#/usr/bin/python3
# -*- coding:utf-8 -*-
#-------------------------
#文件: database.py
#作者: String
#邮箱: 18093329352@163.com
#时间: 17-12-6 下午3:37
#-------------------------

import pymysql

# 连接数据库
def connectData():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='jiangyan1921',
                           db='music',
                           charset='utf8')


# 查询数据库
def checkData():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='jiangyan1921',
                           db='music',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

