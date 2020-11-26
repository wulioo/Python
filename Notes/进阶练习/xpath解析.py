# -*- codeing = utf-8 -*-
# @Time : 2020/9/11 12:33 下午

'''
# --返回多个div对象，然后根据属性查到单一的div
属性定位,固定写法：tree.xpath('//div[@class="song"]')
# --查找属性为song的div,子标签p下的索引位置3
索引定位：tree.xpath('//div[@class="song"]/p[3]')
# --获取文本数据text()函数
tree.xpath('//div[@class='song']//li[5]/a/text()')[0]
# --获取标签a标签属性值
tree.xapth('//div[@class='song']/img/@src')
'''
from lxml import etree
import requests
import os

os.listdir
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

if __name__ == '__main__':

    if not os.path.exists('./美女壁纸'):
        os.mkdir('./美女壁纸')
    url = 'http://pic.netbian.com/4kmeinv/'
    img_reps = requests.get(url, headers=headers).content
    # --实例化好一个etree对象，且将被解析的源码加载到改对象中
    tree = etree.HTML(img_reps)
    print(tree)
    # --截取到div下的图片
    img_src = tree.xpath('//div[@class="slist"]//img')
    for src in img_src:
        src_img = src.xpath('./@src')[0]
        img_url = 'http://pic.netbian.com/' + src_img
        src_title = src.xpath('../b/text()')[0]
        img_path = './美女壁纸/' + src_title+'.jpg'
        try:
            img = requests.get(img_url, headers=headers).content
            with open(img_path, 'wb') as f:
                f.write(img)
        except Exception as result:
            print(result)
