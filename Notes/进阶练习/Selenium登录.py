# -*- codeing = utf-8 -*-
# @Time : 2020/9/11 4:19 下午

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # WebDriverWait的作用是等待某个条件的满足之后再往后运行
import time
import json
import os


class Sina:
    def __init__(self, url, username, password, input_user, input_pwd, input_login):
        self.username = username
        self.password = password
        self.input_user = input_user
        self.input_pwd = input_pwd
        self.input_login = input_login
        self.url = url
        self.__login()

    # --登录获取cookies
    def __login(self):

        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(5)
        print('开始模拟登陆：')
        try:
            # //input[@id="loginname"]
            driver.find_element_by_xpath(self.input_user).click()
            driver.find_element_by_xpath(self.input_user).send_keys(self.username)
            time.sleep(2)
            # ".password > div:nth-child(1) > input:nth-child(1)"
            driver.find_element_by_css_selector(self.input_pwd).click()
            driver.find_element_by_css_selector(self.input_pwd).send_keys(self.password)
            time.sleep(2)
            print('use and pwd succees')
        except:
            print('error')
            # "div.info_list:nth-child(6) > a:nth-child(1)"
        driver.find_element_by_css_selector(self.input_login).click()
        time.sleep(3)
        # --获取cookies，[]列表
        cookies = driver.get_cookies()

        cookie_dict = {}
        for cookie in cookies:
            if 'name' in cookie.keys() and 'value' in cookie.keys():
                # --将cookie字典的key添加到cookie_dict字典中
                cookie_dict[cookie['name']] = cookie['value']

        with open('cookie.txt', 'w') as f:
            f.write(json.dumps(cookies))
            print('cookie保存成功')
        driver.close()
        return cookie_dict

    # --从本地获取cookies
    def get_cookie_cache(self):
        cookies_dict = {}
        if os.path.exists('cookie.txt'):
            # --判断如果本地有cookie文件，则取本地cookies，否则返回空
            with open('cookie.txt', 'r') as f:
                for i in json.loads(f.read()):
                    if 'name' in i.keys() and 'value' in i.keys():
                        cookies_dict[i['name']] = i['value']
        else:
            return cookies_dict
        return cookies_dict

    # --获取cookie，如果不退出cookie，将重新登录
    def get_cookie(self):
        cookie_dict = self.get_cookie_cache()
        if not cookie_dict:
            cookie_dict = self.__login()
        return cookie_dict


if __name__ == '__main__':
    weibo = Sina('https://weibo.com/', '19868922770', 'aa1234bb',
                 '//input[@id="loginname"]',
                 ".password > div:nth-child(1) > input:nth-child(1)",
                 "div.info_list:nth-child(6) > a:nth-child(1)")
