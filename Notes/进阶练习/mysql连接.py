# -*- codeing = utf-8 -*-
# @Time : 2020/9/10 4:43 下午
import pymysql


def save_to_mysql():
    # --建立数据库连接对象
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='aa1234bb', db='py_doub')
    # --使用cursor()方法创建一个游标对象 cursor
    my_cursor = conn.cursor()
    # --sql语句
    insert_sql = """
        insert into info(movice_name,movice_a,movice_title,movice_conntent,movice_eva)values (%s,%s,%s,%s,%s)
    """
    # --
   # my_cursor.execute(insert_sql, (movie[0], movie[2], movie[1][0], movie[3], movie[4], movie[5][1]))
    # --执行sql语句
    conn.commit()
    # --关闭连接
    my_cursor.close()
    conn.close()