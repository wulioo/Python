# -*- codeing = utf-8 -*-
# @Time : 2020/11/17 5:45 下午
from loguru import logger

logger.add("LogDug/demo.log", rotation="12:00", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", filter="", level="DEBUG")