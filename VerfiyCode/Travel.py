# -*- codeing = utf-8 -*-
# @Time : 2020/11/15 7:36 下午
import re
import json
import requests
from config import settings
from VerfiyCode.Chaojiying import Chaojiying_Client
from LogDug.logDug import logger
from urllib.parse import unquote




url = 'https://user.qunar.com/passport/loginx.jsp'
Code_url = 'https://user.qunar.com/captcha/api/image?'


class Travel(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = requests.session()

    @logger.catch()
    def login(self):

        self.session.get('https://user.qunar.com/passport/login.jsp')

        self.getImage()

        self.session.get('https://user.qunar.com/passport/addICK.jsp?ssl')

        self.session.get("https://user.qunar.com/passport/login.jsp?",
                         params={'ret': 'http://user.qunar.com/index/page'})

        sessionid = self.session.get('https://rmcsdf.qunar.com/js/df.js?org_id=ucenter.login&js_type=0').text
        seid = re.findall('sessionId=(.*?)&', sessionid)[0]
        self.session.cookies.update({"QN271": seid})

        code = self.VerfiyCode(1902)
        print("当前验证码为:", code)

        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
        }
        code = input("请输入验证码:")
        data = {
            'loginType': '0',
            'ret': 'http://user.qunar.com/userinfo/account.jsp',
            'username': self.user,
            'password': self.password,
            'remember': '1',
            'vcode': code
        }

        for i in range(20):

            rps = self.session.post(url, headers=headers, data=data).json()
            print(rps)

            if rps['ret'] == True:
                cookies = self.session.cookies
                return rps, cookies

    def getImage(self):
        parmas = {
            'k': '{en7mni(z',
            'p': 'ucenter_login',
            'c': 'ef7d278eca6d25aa6aec7272d57f0a9a'
        }
        reps = self.session.get(Code_url, params=parmas)
        cookies = dict(reps.cookies)
        with open("code.png", "wb") as f:
            f.write(reps.content)
        return cookies

    def VerfiyCode(self, number):

        Code = Chaojiying_Client('a541541000', 'aa1234bb', 908189)
        try:
            img = open('code.png', 'rb').read()

        except Exception as f:
            print('error:', f)
        RandCode = Code.PostPic(img, number)['pic_str']

        return RandCode

    def Urldeco(self, url,cookies):
        url_ = url['data']['redirect']
        url_ = unquote(url_)
        rep = requests.get(url_, cookies=cookies).text
        print(rep)


if __name__ == '__main__':
    travel = Travel('19868922770', 'aa1234bb')
    message,cookies = travel.login()
    travel.Urldeco(message,cookies)
