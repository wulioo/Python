# -*- codeing = utf-8 -*-
# @Time : 2020/9/16 2:42 下午

import pymysql
import json
import os
from flask import Flask,request
app=Flask(__name__)

'''
带有入参的接口查询
'''

@app.route('/index',methods=['post'])


def indextest():
    title =request.json.get('title')
    data1=getconn(title)
    return data1

def getconn(title):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='aa1234bb', db='py_doub')
    # --使用cursor()方法创建一个游标对象 cursor
    my_cursor = conn.cursor()
    sql = "select * from doubae1 where movice_title='{}'".format(title)
    my_cursor.execute(sql)
    # --查找所有行数据
    data = my_cursor.fetchall()
    data_li = []
    for i in data:
        dict_li = {'id': i[0], 'movie': i[1], 'img': i[2], 'title': i[3], 'content': i[4]}
        # print(dict_li)
        data_li.append(dict_li)

    # json.dumps将python对象转换为json字符串，ensure_ascii中文编码，indent显示多少行缩进
    data = json.dumps(data_li, ensure_ascii=False, indent=4)
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
