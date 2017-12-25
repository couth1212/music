#/usr/bin/python
# -*- coding:utf-8 -*-
#-------------------------
#文件: analysisAuthor.py
#作者: String
#邮箱: 18093329352@163.com
#时间: 17-12-6 下午3:29
#-------------------------

from wordcloud import WordCloud
from util import database
from pylab import *
from matplotlib.font_manager import FontProperties
chinese_font = FontProperties(fname='/usr/share/fonts/MyFonts/yahei_mono.ttf')

# 生成标题词云
def titleWordCloud():
    cursor.execute('select title, inq from music')
    results = cursor.fetchall()
    str = ''
    for x in results:
        for t in range(int(int(x['inq'])/1000)):
            str = str + x['title'] + " "
    font = 'util/wqy-microhei.ttc'
    wc = WordCloud(collocations=False,
                   font_path=font,
                   width=2000,
                   height=2000,
                   margin=2).generate(str)
    wc.to_file('picture/titlePic.png')

# 生成作者词云
def authorWordCloud():
    cursor.execute('select author from music')
    results = cursor.fetchall()
    str = ''
    for x in results:
        str = str + x['author'] + " "
    font = 'util/wqy-microhei.ttc'
    wc = WordCloud(collocations=False,
                   font_path=font,
                   width=2000,
                   height=2000,
                   margin=2).generate(str)
    wc.to_file('picture/authorPic.png')

# 获得作者数据列表  为绘制折线图做准备
def authorBrokenLine():
    cursor.execute('select author from music')
    results = cursor.fetchall()
    li = []
    # 获得作者数据
    for x in results:
        li.append(x['author'])
    dict = {}
    # 对作者数据进行统计
    for x in li:
        count = 0
        for t in li:
            if x == t:
                count += 1
        dict[x] = count
    # 提出作品大于5个的作者
    name = []
    num = []
    for x in dict:
        if dict[x] > 7:
            name.append(x)
            num.append(dict[x])
    t = []
    t.append(name)
    t.append(num)
    print(t)
    return t

# 绘制折线图
def pointBrokenLine(t):
    name = t[0]
    num = t[1]
    plt.clf()  # 清空画布
    # 添加绘图数据
    plt.plot(range(1,10), num)
    # xy轴标明
    plt.xlabel("作者", fontproperties=chinese_font)
    plt.ylabel("作品数", fontproperties=chinese_font)
    # 标题
    plt.title('作品超过七个的创作者', fontproperties=chinese_font)
    legend(['图例'], prop=chinese_font)
    # 设置横坐标
    plt.xticks(range(1,10), name, rotation=0.2, fontproperties=chinese_font)
    plt.show()

# 绘制饼状图
def pointPie(t):
    name = t[0]
    num = t[1]
    plt.clf()
    # plt.title('作者饼图', fontproperties=chinese_font)
    t = plt.pie(num,labels=name, autopct="%1.2f%%", shadow=True)
    # 将pie对象中的text设置为中文字体
    for font in t[1]:
        font.set_fontproperties(mpl.font_manager.FontProperties(
            fname='/usr/share/fonts/MyFonts/yahei_mono.ttf'))
    plt.axis('equal')
    plt.show()


# 生成柱状图
def pointbar(t):
    name = t[0]
    num = t[1]
    plt.clf()  # 清空画布
    plt.bar(range(1,10), num, align="center",color="#2dd789")
    plt.xlabel("作者", fontproperties=chinese_font)
    plt.ylabel("作品数", fontproperties=chinese_font)
    plt.title('作品超过七个的创作者', fontproperties=chinese_font)
    plt.xticks(range(1,10), name, rotation=0.2, fontproperties=chinese_font)
    plt.show()



if __name__ == '__main__':
    # 连接数据库
    conn = database.checkData()
    # 创建游标
    cursor = conn.cursor()
    conn.commit()
    # print("连接成功")
    titleWordCloud()
    authorWordCloud()
    t = authorBrokenLine()
    pointBrokenLine(t)
    pointPie(t)
    pointbar(t)
    cursor.close()
    conn.close()

