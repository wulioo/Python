# -*- codeing = utf-8 -*-
# @Time : 2020/9/14 7:43 下午

import requests
from lxml import etree
import re
# -- 导入一个线程池的包
from multiprocessing.dummy import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

url = 'https://www.pearvideo.com/category_5'

page_text = requests.get(url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []  # --存储视频连接
for li in li_list:
    detail_href = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    movie_title = li.xpath('.//div[@class="vervideo-title"]/text()')[0] + '.mp4'
    # --对详情页发起请求
    movie_details = requests.get(detail_href, headers=headers).text
    # --从详情页面解析出视频地址（url）
    movie = re.findall('srcUrl="(.*?)",vdoUrl', movie_details, re.S)[0]
    dict = {
        'name': movie_title,
        'movie_url': movie
    }
    urls.append(dict)



def get_video_data(dict):
    # 获取dic字典的url连接
    url = dict['movie_url']
    print(dict['name'], '正在下载')
    data = requests.get(url, headers=headers).content
    # --持久化存储操作
    with open(dict['name'], 'wb') as f:
        f.write(data)
        print(dict['name'], '下载成功')

# --使用线程池对视频数据进行请求（较为耗时间的阻塞操作）
# -实例化线程池对象
pool = Pool(4)
# -进行map方法应用，
pool.map(get_video_data, urls)
# --关闭线程池
pool.close()
# --join让主线程等待子线程
pool.join()