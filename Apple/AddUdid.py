# -*- codeing = utf-8 -*-
# @Time : 2020/11/25 7:17 下午

from loguru import logger
from Email.getEmail import Email

class AddUdid():
    def __init__(self):
        self.udid = self.add()

    def add(self):
        e = Email('zhengdh@huabo.tech', 'Aa1234bb', 'pop.exmail.qq.com')
        '' \
        ''
        udid=e.udid
        logger.info(udid)
if __name__ == '__main__':
    udid = AddUdid()
