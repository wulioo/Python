# -*- codeing = utf-8 -*-
# @Time : 2020/9/10 10:26 下午

import requests
import os
from bs4 import BeautifulSoup
import threading
from multiprocessing.dummy import Pool
import time

# --类 面向对象 继承 继承的父类是写在当前类名的（）中
class MyThread(threading.Thread):
    def run(self):
        CrawlSourcePage()


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

url = 'http://www.shicimingju.com/book/sanguoyanyi.html'

def get_url():
    reps = requests.get(url, headers=headers).text
    soup = BeautifulSoup(reps, 'lxml')
    return soup

def CrawlSourcePage():
    soup = get_url()
    # --select 选择器 选择 calss属性.book-mulu 层级下的ul 下的a标签
    book_a = soup.select('.book-mulu > ul a')
    if not os.path.exists('./三国演义'):
        os.mkdir('./三国演义')
    for a in book_a:
        a_href = 'http://www.shicimingju.com' + a['href']
        book_page_content = requests.get(a_href, headers=headers).text
        # --创建bs4对象来解析获取到的内容详情页面
        content_ = BeautifulSoup(book_page_content, 'lxml')
        # --find遍历出内容章节标题
        title = content_.find('h1').text
        # --标题名
        title_path = './三国演义/' + title + '.text'
        print(title)
        # --find遍历出div标签下的所有内容
        content = content_.find('div', class_="chapter_content").text
        # print(content)

        with open(title_path, 'wb') as f:
            f.write(content.encode('utf-8'))
            print('正在爬取')

if __name__ == '__main__':
    t=MyThread()
    t.start()
    for i in range(100):
          time.sleep(1)
          print(i)

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, url, newdir,CrawledURLs):
        threading.Thread.__init__(self)