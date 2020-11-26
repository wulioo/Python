# -*- codeing = utf-8 -*-
# @Time : 2020/8/25 1:55 下午

import urllib.request
from http import cookiejar
from urllib import request
from selenium import webdriver
import time
url = "http://i.baidu.com/"

cookiea = []
if __name__ == '__main__':
    # # --声明一个CookieJar对象实例来保存cookie
    # cookie = cookiejar.CookieJar()
    # # --利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器，也就CookieHandler
    # handler = request.HTTPCookieProcessor(cookie)
    # # --通过CookieHandler创建opener
    # opener = request.build_opener(handler)
    # # --此处的open方法打开网页
    # responce = opener.open('https://passport.baidu.com/v2/api/?login')
    #
    #
    # for item in cookie:
    #     # --将遍历的cookies存入字典
    #     cookies = {'name':item.name,'value':item.value}
    #     # --将字典的cookies存入列表
    #     #cookiea.append(cookies)
    #     print(cookies)
    # haders = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    #

    driver = webdriver.Chrome()
    driver.get('https://passport.baidu.com/v2/api/?login')

    # driver.add_cookie(cookie_dict=cookies)
    driver.get('http://i.baidu.com/')


