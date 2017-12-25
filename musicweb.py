#/usr/bin/python
# -*- coding:utf-8 -*-
#-------------------------
#文件: musicweb.py
#作者: String
#邮箱: 18093329352@163.com
#时间: 17-11-29 下午8:23
#-------------------------

from tornado import web, httpserver, ioloop
import util.database


# 路由 主页面
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/index.html')

    def post(self, *args, **kwargs):
        print(USER_NAME)
        kw = self.get_argument('kw')
        print(kw)
        return kw
        # cursor.execute('select netacc, netname from uesr WHERE netacc LIKE "%{}%"'.format(kw))
        # results = cursor.fetchall()
        # conn.commit()
        # for x in results:
        #     print(x)

    # # 保存用户搜索数据
    # def saveUserdata(kw):
    #     filename = 'userdata/' + USER_NAME + '.txt'
    #     with open(filename, 'w+') as f:
    #         f.write(kw)
    #     print('写入成功')

# 路由 注册页面
class SignHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/sign.html')

    def post(self, *args, **kwargs):
        # 获得页面post信息
        netname = self.get_argument('netname')
        netacc = self.get_argument('netacc')
        passwdone = self.get_argument('passwdone')
        passwdtwo = self.get_argument('passwdtwo')
        sex = self.get_argument('sex')
        phone = self.get_argument('phone')
        # 判断信息是否完整
        if netacc and netname and passwdtwo and passwdone and sex and phone:
            if passwdone and passwdtwo:
                cursor.execute('insert into uesr(netacc, netname, passwd, phone, sex) VALUE ({}, {}, {}, {}, {})'
                               .format(netacc, netname, passwdone, str(phone), sex))
                conn.commit()
                self.redirect('/login')
            else:
                self.write('两次输入的密码不一样！')
        else:
            self.write('请将信息填写完整！')


# 路由 登陆界面
class loginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/login.html')

    def post(self, *args, **kwargs):
        # 获得登陆信息
        netacc = self.get_argument('netacc')
        passwd = self.get_argument('passwd')
        # 进行判断
        if netacc and passwd:
            try:
                cursor.execute('select netacc, netname from uesr WHERE netacc = {}'.format(netacc))
                results = cursor.fetchall()[0]
                conn.commit()
                # 判断密码是否正确
                if results['netname'] == passwd:
                    # self.redirect()返回页面网址  实现页面跳转
                    USER_NAME = netacc
                    self.redirect('/index')
                else:
                    self.write('请检查账号或密码是否正确！')
            except Exception as e:
                self.write('账号不存在')
        else:
            self.write('请填写完整信息！')


#路由注册
application = web.Application([(r'/index$', MainPageHandler),
                               (r'/sign', SignHandler),
                               (r'/login', loginHandler),])


if __name__ == '__main__':
    USER_NAME = None
    # 链接数据库
    conn = database.checkData()
    # 创建游标
    cursor = conn.cursor()
    # 启动服务
    http_server = httpserver.HTTPServer(application)
    # 端口监听
    http_server.listen(8080)
    ioloop.IOLoop.current().start()


