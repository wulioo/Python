# -*- codeing = utf-8 -*-
# @Time : 2020/8/25 8:58 上午

import lxml.html
from lxml import etree

#   -----------案列（一）----------
html = '''
<html>
    <head>
        <title>测试</title>
    </head>
    <body>
        <div class="useful">
            <ul>
            <li class="info">我需要的信息1</Li>
            <li class="info">我需要的信息2</Li>
            <li class="info">我需要的信息3</li>
            </ul>
        </div>
    </body>
</html>
'''
# 解析html页面，返回单个元素/文档
selector = lxml.html.fromstring(html)

"""
# 截取div/ul/li 下的的标签内容,以列表的方式返回内容
info = selector.xpath('//div[@class="useful"]/ul/li/text()')
# 截取div 已starts-with()函数查找test相同部分的开头
info = selector.xpath('//div[starts-with(@属性名, "test")]/text()')
# 截取div 已contains函数查找属性值包括key字符串的标签
info = selector.xpath('//div[contains(@属性名, "key")]/text()')
#print(info)
"""

#   -----------案列（二）----------

"""
# 导入lxml 扩展IPA etree
from lxml import etree
# 用etree.HTML函数对html页面进行初始化
htmls = etree.HTML(html)
# 利用xpath截取div节点下的所有内容 利用string(path)
result = htmls.xpath('string(//*[@id="content"]/div/div[1]/ol/li[1]/div)')
print(result)
"""