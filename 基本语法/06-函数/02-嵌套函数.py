# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 15:39
# @Author  : wuwenxi

import random

"""
函数内可以定义函数, 定义在函数内部的函数不能被外部直接调用
"""


def funb():
    print('funb')


def funa():
    def funb():
        print('funb')

    funb()
    print("funa")


funa()

random.randint(1, 6)
