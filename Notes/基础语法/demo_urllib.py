# -*- codeing = utf-8 -*-
# @Time : 2020/8/23 11:45 上午

import urllib.request
import urllib.parse
# ----获取一个Get请求
'''
responce = urllib.request.urlopen("http://www.baidu.com")
#----对网页源代码进行UTF-8解析,decode将编码转换python内部的unicode
print(responce.read().decode('utf-8'))
'''

# ----获取一个post请求
'''
try:
    Data = bytes(urllib.parse.urlencode({
        'i': "my",
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15981549260044',
        'sign': '046e56d712eaa3a2909e2127c7b36245',
        'lts': '1598154926004',
        'bv': '9b5404b204b311eab113da940e6f747b',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'}), encoding="utf-8")
except Exception as result:
    print(result)
try:
    responce = urllib.request.urlopen("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule", data= Data)
    print(responce.read().decode('utf-8'))
except Exception as result:
    print(result)
'''

# ---获取头部请求
'''
responce = urllib.request.urlopen("http://baidu.com")
print(responce.getheaders())
'''

# ----我不是爬虫，是一个浏览器
'''
url = "http://www.baidu.com"

# 构建了一个Requst请求
req = urllib.request.Request(url=url)
req.add_header('Use-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')
responce = urllib.request.urlopen(req)
print(responce.read().decode('utf-8'))
'''

# ------------构建完整的请求---------------

url = "http://www.baidu.com"
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}      # 隐藏头部请求信息
data = bytes(urllib.parse.urlencode({'name': 'hellow'}), encoding='utf-8')      # 传输data参数，必须以bytes字节流传输数据
req = urllib.request.Request(url, data=data, headers=headers)                   # 构建一个Request请求
responce = urllib.request.urlopen(req)                                          # 打开一个URL网页，发起请求
print(responce.read().decode("utf-8"))



