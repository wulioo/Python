# -*- codeing = utf-8 -*-
# @Time : 2020/9/9 11:03 下午
'''
分页操作爬取
'''

import requests
import re
import os

if __name__ == '__main__':

    # ----设置通用分页url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    # ----判断是否存在糗图这个文件夹，如果不存在则当前目录下创建
    if not os.path.exists('./qiutu_img'):
        os.mkdir('./qiutu_img')

    # print(img_url)
    for page in range(1, 10):
        # --对应页码的url
        page_url = format(url % page)
        reps = requests.get(page_url, headers).text
        re_imge = '<div class="thumb">.*?<img src="(.*?)" alt.*?></div>'
        img_url = re.findall(re_imge, reps, re.S)
        for img in img_url:
            img_url = 'https:' + img
            # ----content请求二进制的数据
            reps = requests.get(img_url, headers).content
            # ----持久化存储的文件名
            img_name = img_name = img.split('/')[-1]
            qiutu_path = './qiutu_img/' + img_name
            with open(qiutu_path, 'wb') as f:
                f.write(reps)
                print('正在下载')
