# -*- codeing = utf-8 -*-
# @Time : 2020/9/22 10:47 下午
import sys
from loguru import logger



# --创建一个日志文件，每天12点进行分割 format格式化 time时间 level级别 message信息 filter过滤
#logger.add("demo.log", rotation="12:00", format="{time} {level} {message}", filter="", level="INFO")
logger.add(sys.stderr, colorize=True, format="<green>{time}</green> <level>{message}</level>",level="INFO")

logger.debug('这是一条Debug日志')
logger.info("这是一条INFO日志")
