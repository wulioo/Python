# -*- codeing = utf-8 -*-
# @Time : 2020/11/18 10:00 上午

from stem import Signal
from stem.control import Controller
import requests
import json
from config import settings


def switchIP():
    with Controller.from_port() as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    # ENV_FOR_DYNACONF = dev


def main():

    proxy = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    for i in range(20):
        rps = requests.get('https://httpbin.org/ip', proxies=dict(settings.get('tor.proxy')))
        print(settings.get('tor.proxy'))
        print(json.loads(rps.content))


if __name__ == '__main__':
    main()
