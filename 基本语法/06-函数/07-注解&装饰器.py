# -*- coding: utf-8 -*-
# @Time    : 2025/7/28 22:16
# @Author  : wuwenxi

import random
import time

from functools import wraps

"""
functools模块的wraps函数也是一个装饰器，我们将它放在wrapper函数上，这个装饰器可以帮我们保留被装饰之前的函数，
"""


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# 调用装饰后的函数会记录执行时间
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')


def decorator(planes):
    def func(fn):
        fn.planes = planes
        return fn

    return func


@decorator(1)
def one():
    print('this is one')


@decorator(2)
def two():
    print('this is two')


default = [
    one,
    two
]

for f in default:
    print(f.planes)
    f()
