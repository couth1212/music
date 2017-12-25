#/usr/bin/python
# -*- coding:utf-8 -*-
#-------------------------
#文件: data.py
#作者: String
#邮箱: 18093329352@163.com
#时间: 17-12-6 下午12:28
#-------------------------

import csv
from util import database


def getData():
    cursor.execute('select * from music')
    results = cursor.fetchall()
    headers = ['id', 'title',  'author', 'musictype',  'inq',  'href']
    with open('data.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(results)
    conn.commit()
    cursor.execute('select title from music')
    results = cursor.fetchall()
    for x in results:
        with open('titlePic.txt', 'a+') as f:
            f.write(x['title'] + ' ')
    print("写入成功")

if __name__ == '__main__':
    # 链接数据库
    conn = database.checkData()
    # 创建游标
    cursor = conn.cursor()
    getData()
    cursor.close()
    conn.close()