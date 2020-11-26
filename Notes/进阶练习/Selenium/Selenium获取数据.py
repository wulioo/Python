# -*- codeing = utf-8 -*-
# @Time : 2020/9/19 12:37 下午
from lxml import etree
from selenium import webdriver
from time import sleep

url = 'https://www.iqiyi.com'

# --设置无界面浏览
chrome = webdriver.ChromeOptions()
chrome.add_argument('--headless')
chrome.add_argument('--disable-gpu')
# --实例化一个谷歌浏览器对象（传浏览器驱动路径path）
dev = webdriver.Chrome(chrome_options=chrome)

# --让浏览器发起一个url请求
dev.get(url)

# --page_source获取浏览器当前页面的源码数据
html = dev.page_source

# --创建etree对象解析源码网页
html_ = etree.HTML(html)
# --获取title
ht_title = html_.xpath('//*[@class="qy-mod-list mb"]/ul//a/@title')
for i in ht_title:
    print(i)
sleep(5)
dev.quit()
