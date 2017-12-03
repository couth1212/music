#/usr/bin/python
# -*- coding:utf-8 -*-
#-------------------------
#文件: musicweb.py
#作者: String
#邮箱: 18093329352@163.com
#时间: 17-11-29 下午8:23
#-------------------------

from tornado import web, httpserver, ioloop
import pymysql

# 路由 主页面
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 主页面
        self.render('templates/index.html')


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
                # 将用户注册信息添加到数据库
                cursor.execute('insert into uesr(netacc, netname, passwd, phone ,sex) value({},{},{},{},{})'
                               .format(netacc, netname, passwdone, str(phone), sex))
                conn.commit()
                print("注册成功")
            else:
                self.write('两次输入的密码不一样！请重试')
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
            cursor.execute('select * from uesr')
            results = cursor.fetchall()
            print(results)
        else:
            self.write('请将信息填写完整！')

#路由注册
application = web.Application([(r'/index', MainPageHandler),
                               (r'/sign', SignHandler),
                               (r'/login', loginHandler),])


if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='**************',
                           db='music',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = conn.cursor()
    # 启动服务
    http_server = httpserver.HTTPServer(application)
    # 端口监听
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
    # 链接数据库

