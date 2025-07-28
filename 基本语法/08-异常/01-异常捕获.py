# -*- coding: utf-8 -*-
# @Time    : 2025/5/27 11:15
# @Author  : wuwenxi

import logging
from logging import getLogger, getLoggerClass

logging.basicConfig(level=logging.ERROR)

try:
    print(a)
except NameError as e:
    print(e)


def func():
    raise Exception("不支持操作的方法")


try:
    func()
except Exception as e:
    print(str(e))
    logging.error('使用raise抛出异常', exc_info=True)
