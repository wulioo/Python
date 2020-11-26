# -*- codeing = utf-8 -*-
# @Time : 2020/11/17 5:45 下午
from loguru import logger

# 将日志打印到log文件
# logger.add("LogDug/demo.log", rotation="12:00", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", filter="", level="DEBUG")

logger.debug('调试消息')
logger.info('普通消息')
logger.warning('警告消息')
logger.error('错误消息')
logger.critical('严重错误消息')
logger.success('成功调用')
