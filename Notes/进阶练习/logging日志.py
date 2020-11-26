# -*- codeing = utf-8 -*-
# @Time : 2020/9/22 3:46 下午

import logging

# --使用baseConfig()来指定日志输出级别

'''
 # 输出格式和添加一些公共信息
 --(filename='demo.log', filemode='w', level=logging.DEBUG) 日志文件,日志添加模式,日志级别

 --(format="%(asctime)s | %(levelname)s | %(message)s | ", level=logging.DEBUG)格式化输出
    2020-09-22 20:14:20,140 | DEBUG | 姓名:zdh，年龄:18 |
'''
name = 'zdh'
age = 18
logging.basicConfig(format="%(asctime)s | %(levelname)5s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.DEBUG)
logging.debug("姓名:{}，年龄:{}".format(name, age))

# --记录器
logger = logging.getLogger()
# --修改日志级别为debug，必须指定级别DEBUG
logger.setLevel(logging.DEBUG)

# --处理器handler,打印到console
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

# --文件处理器handler,没有指定文件处理级别，将使用记录器的级别
fileHander = logging.FileHandler(filename='../Introduction/baidu_tb/demo.log')
fileHander.setLevel(logging.INFO)

# --formatter格式,格式可以设置多个
ftr = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# --给处理器设置格式
consoleHandler.setFormatter(ftr)
fileHander.setFormatter(ftr)

# --记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHander)

# --定义一个过滤器过来zdh开头的，并且将过滤器添加到logger
flt = logging.Filter("zdh")
logger.addFilter(flt)

# --打印日志，用自己创建的记录笔
logger.info('my is log')
logger.debug('my is debug')