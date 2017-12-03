#/usr/bin/python
# -*- coding:utf-8 -*-
#-------------------------
# 文件: music.py
# 作者: String
# 邮箱: 18093329352@163.com
# 时间: 17-11-22 下午10:19
#-------------------------

import requests
import pymysql
import re
import urllib


def main():
    index = 0        
    while(index <= 25):
        url = 'http://www.htqyy.com/top/musicList/hot?pageIndex={}&pageSize=20'.format(str(index))
        index  = 1 + index
        html = gethtml(url)
        getcontent(html)
    cursor.close()
    conn.close()


def gethtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    html = requests.get(url, headers=headers)
    print("正在下载---> " + url)
    tag = r'<li class="mItem">(.*?)</li>'
    html = re.findall(tag, html.text, re.S|re.M)
    return html
    

def getcontent(html):
    tag_title = r'<span class="title"><a href=".*?" target="play" title=".*?" sid=".*?">(.*?)</a></span>'
    tag_href = r'<span class="title"><a href="(.*?)" target="play" title=".*?" sid=".*?">.*?</a></span>'
    tag_author = r'<span class="artistName"><a href=".*?" title=".*?" target="_blank">(.*?)</a></span>'
    tag_musictype = r'<span class="albumName"><a href=".*?" title=".*?" target="_blank">(.*?)</a></span>'
    tag_inq = r'<span class="playCount">(.*?)</span>'
    for x in html:
        title = re.findall(tag_title, x)
        href1 = re.findall(tag_href, x)
        author = re.findall(tag_author, x)
        musictype = re.findall(tag_musictype, x)
        inq1 = re.findall(tag_inq, x)
        href = 'http://f1.htqyy.com{}/mp3/18'.format(str(href1[0]))
        inq = re.findall(r'\d*', inq1[0])
        cursor.execute('insert into music(title, href, author, musictype, inq) value("{}", "{}", "{}", "{}", "{}")'.format(
            title[0], href, author[0], musictype[0], int(inq[0])))
        conn.commit()
        print('正在添加---> ', title[0], href, author[0], musictype[0], str(inq[0]))

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='*************',
                           db='music',
                           charset='utf8')
    cursor = conn.cursor()
    conn.commit()
    print("链接成功")
    main()
