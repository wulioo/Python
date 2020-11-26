# -*- codeing = utf-8 -*-
# @Time : 2020/8/26 12:14 上午

import sqlite3
# ----连接数据库-----
conn = sqlite3.connect("test.db")

print("opened database successfully")

c = conn.cursor() #获取游标

# sql='''
#     create table company
#         (id int primary key not null,
#          name text not null,
#          age int not null,
#          address char(50),
#          salary real);
# '''
sql1 = '''
    insert into company (id,name,age,address,salary)
     values ('1','zhangsan',32,"ceasd",8000)
'''
c.execute(sql1)      #执行sql语句
conn.commit()        #提交数据库
conn.close()         #关闭连接