# -*- codeing = utf-8 -*-
# @Time : 2020/9/20 12:09 上午
from lxml import etree
import requests
import os
from chaojiying import Chaojiying_Client

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
src = '//*[@id="imgCode"]/@src'
src_head = 'https://so.gushiwen.cn'


class verification():
    def __init__(self, url, src, src_head):
        self.src = src
        self.url = url
        self.src_head = src_head
        self.verif_img()

    def get_verif(self):
        res = requests.get(self.url).text
        return res

    def verif_img(self):

        etr = etree.HTML(self.get_verif())
        src = etr.xpath(self.src)[0]
        src = self.src_head + src
        try:
            src_img = requests.get(src).content

        except Exception as result:
            print(result)
        else:
            try:
                if not os.path.exists('验证码'):
                    os.mkdir('验证码')
            except Exception as f:
                print(f)

            with open('验证码/RandCode.jpg', 'wb') as f:
                f.write(src_img)


#if __name__ == '__main__':
    # veri = verification(url, src, src_head)
    # chaojiying = Chaojiying_Client('a541541000', 'aa1234bb', '908189')
    # im = open('验证码/RandCode.jpg', 'rb').read()
    # RandCode = chaojiying.PostPic(im, 1004)['pic_str']
