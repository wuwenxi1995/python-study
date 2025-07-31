# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 19:52
# @Author  : wuwenxi

"""
 三目运算： [表达式1或结果1] if [条件语句] else [表达式2或结果2] ,条件为真时 执行if前面的语句 为假执行else后面语句
"""

a, b = 1, 2

print(a) if a > b else print(b)

print(b - a) if a < b else print(a - b)
