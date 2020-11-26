# -*- codeing = utf-8 -*-
# @Time : 2020/9/20 8:50 上午

import requests
from chaojiying import Chaojiying_Client
from Verification import verification
from urllib import parse
from loguru_ import logger

logger.add("demo.log", rotation="12:00", format="{time} {level} {message}", filter="", level="INFO")

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
login_url = 'https://so.gushiwen.cn/user/collect.aspx'
src = '//*[@id="imgCode"]/@src'
src_head = 'https://so.gushiwen.cn'


class singin():
    def __init__(self):
        pass
    @logger.catch()
    def get_login(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Host': 'so.gushiwen.cn',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'login=flase; gsw2017user=1272876%7c95725811675DF39CE970DCA5B7AD7D33; gswEmail=a541541000%40163.com; gswZhanghao=a541541000%40163.com; login=flase; wxopenid=defoaltid; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1600565753; Hm_lvt_9007fab6814e892d3020a64454da5a55=1600530223; codeyzgswso=bdb1491df7539274; wsEmail=a541541000%40163.com; ASP.NET_SessionId=0afggpo5spkz3ldxf2sfvbpx'

        }
        data = {
            '__VIEWSTATE': 'Gbu46tg+aar2jc+QWW34oxbEhwz4ED/9qMKok0IxciV/DwZ+OLcoNa2EgMy5wogt2tjL0W3PPV/gUOdBew9thEUAtwcjxm8Y5/uEp1RXhnw82BubWV5bI/6gfAo=',
            '__VIEWSTATEGENERATOR': 'C93BE1AE',
            'from': 'http://so.gushiwen.cn/user/collect.aspx',
            'email': 'a541541000@163.com',
            'pwd': 'aa1234bb',
            'code': 'verifi',
            'denglu': '登录'
        }
        # , data = parse.urlencode(data).encode('utf-8')
        reps = requests.get(login_url, headers=headers)
        #reps.encoding = "gbk"
        reps.encoding="ISO-8859-1"
        logger.info(reps.text)
        #print()


if __name__ == '__main__':
    veri = verification(url, src, src_head)
  #  chaojiying = Chaojiying_Client('a541541000', 'aa1234bb', '908189')
    # try:
    #     im = open('验证码/RandCode.jpg', 'rb').read()
    # except Exception:
    #     print('error')
    # RandCode = chaojiying.PostPic(im, 1004)['pic_str']
    # print(RandCode)
    sig = singin()
    sig.get_login()
