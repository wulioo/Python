# -*- codeing = utf-8 -*-
# @Time : 2020/8/23 3:04 下午

from bs4 import BeautifulSoup
import re

file = open("./baidu.html", "rb")
html = file.read()
# BeautifulSoup解析html网页，用html.parser解析器来解析
bs = BeautifulSoup(html, "html.parser")

'''
# 1.Tag 标签及其内容，拿到第一个内容
print(type(bs.title))
#  Tag标签里面的内容(字符串)（用的较多）
print(bs.title.string)
#  Tag拿到标签里面属性
print(bs.title.attrs)
'''

# ----------------------------------------

# 文档的遍历

'''
# ---------文档的搜索常用
# 字符串过滤：查找字符串完全匹配的内容
t_list = bs.find_all('a')
'''
# ---------方法：传入一个函数，根据函数的要求来进行搜索


# -----css选择器------
# bs.select('a')通过标签a来进行查找并且循环出来
# bs.select('.bt_button')通过类名来进行查找
# bs.select('#id') 通过ID来进行查找
# bs.select('a[class='bri']')通过a标签的class属性来进行查找
# bs.select('head > title')通过子标签来进行查找
t_list = bs.select('a')
for i in t_list:
    print(i)

# ------案列（一）-------
"""
selectdiv = BeautifulSoup(html, "html.parser")
info = selectdiv.find(class_="info")
al_li = info.find_all("li")
for li in al_li:
    print(li)
#---(1)先抓大在抓小，创建一个Beautifulsoup对象
#---(2)根据标签div class="info" 运用了find()函数查找，find返回一个对象，如果有多个条件，只返回一个对象
#---(3)然后在这个内容只上利用find_all函数，继续查找li标签的内容，find_all返回一个列表，没满足要求返回空列表
#---(4)content = selectdiv.find_all(class_=re.compile('iam'))可以使用正则表达式来进行查找内容
"""
