#/usr/bin/python
# -*- coding:utf-8 -*-
#-------------------------
#文件: analysisType.py
#作者: String
#邮箱: 18093329352@163.com
#时间: 17-12-7 上午11:12
#-------------------------

from wordcloud import WordCloud
from util import database
from pylab import *
from matplotlib.font_manager import FontProperties
chinese_font = FontProperties(fname='/usr/share/fonts/MyFonts/yahei_mono.ttf')

# 生成标题词云
def typeWordCloud():
    cursor.execute('select musictype from music')
    results = cursor.fetchall()
    print(results)
    str = ''
    for x in results:
        str = str + x['musictype'] + " "
    font = 'util/wqy-microhei.ttc'
    wc = WordCloud(collocations=False,
                   font_path=font,
                   width=2000,
                   height=2000,
                   margin=2).generate(str)
    wc.to_file('picture/typePic.png')

# 制作饼图
def pointPie():
    cursor.execute('select musictype from music WHERE musictype LIKE "%轻音乐%"')
    music_qin = len(cursor.fetchall())
    conn.commit()
    cursor.execute('select musictype from music WHERE musictype LIKE "%钢琴%"')
    music_piano = len(cursor.fetchall())
    conn.commit()
    cursor.execute('select musictype from music WHERE musictype LIKE "%纯音乐%"')
    music_chun = len(cursor.fetchall())
    conn.commit()
    cursor.execute('select musictype from music WHERE musictype LIKE "%佛教%"')
    music_fo = len(cursor.fetchall())
    conn.commit()
    cursor.execute('select musictype from music WHERE musictype LIKE "%影视%"')
    music_film = len(cursor.fetchall())
    conn.commit()
    t = plt.pie([music_qin, music_piano, music_chun, music_fo, music_film], labels=[u'轻音乐', u'钢琴', u'纯音乐', u'佛教', u'影视'],autopct="%1.2f%%", shadow=True)
    # 将pie对象中的text设置为中文字体
    for font in t[1]:
        font.set_fontproperties(mpl.font_manager.FontProperties(
            fname='/usr/share/fonts/MyFonts/yahei_mono.ttf'))
    plt.axis('equal')
    plt.show()
    return [[music_qin, music_piano, music_chun, music_fo, music_film], [u'轻音乐', u'钢琴', u'纯音乐', u'佛教', u'影视']]

# 绘制柱状图
def pointBar(li):
    name = li[1]
    num = li[0]
    plt.clf()  # 清空画布
    plt.bar(range(1,len(name)+1), num, align="center", color="#2dd789")
    plt.xlabel("标签", fontproperties=chinese_font)
    plt.ylabel("数量", fontproperties=chinese_font)
    plt.title('标签数量图', fontproperties=chinese_font)
    plt.xticks(range(1,len(name)+1), name, rotation=0.2, fontproperties=chinese_font)
    plt.show()


if __name__ == '__main__':
    # 连接数据库
    conn = database.checkData()
    # 创建游标
    cursor = conn.cursor()
    conn.commit()
    # print("连接成功")
    typeWordCloud()
    li = pointPie()
    pointBar(li)
    cursor.close()
    conn.close()