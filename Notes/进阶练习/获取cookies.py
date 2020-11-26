# -*- codeing = utf-8 -*-
# @Time : 2020/9/11 4:19 下午

import requests
from http import cookiejar


class sigin:
    def __init__(self, url, home_url):
        self.url = url
        self.home_url = home_url

    def login(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
        }
        data = {
            'ck': '',
            'name': 'a541541000@163.com',
            'password': 'aa1234bb',
            'remember': 'false'
        }
        reps = requests.post(self.url, headers=headers, data=data)
        # 获取cookies
        cookies = requests.utils.dict_from_cookiejar(reps.cookies)
        str_ck = ''
        for k, v in cookies.items():
            str_ck = str_ck + k + '=' + v + ';'
        return str_ck

        # with open('./douban.html','w') as f:
        #    f.write(reps)

    def get_home(self, str):
        # cookie = self.__login()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Cookie': str
        }
        reps = requests.get(self.home_url, headers=headers).text
        print(reps)


if __name__ == '__main__':
    db = sigin('https://accounts.douban.com/j/mobile/login/basic', 'https://www.douban.com/')
    cookie = db.login()
    db.get_home(cookie)
