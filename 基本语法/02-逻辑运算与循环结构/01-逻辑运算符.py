# -*- coding: utf-8 -*-
# @Time    : 2025/5/20 10:19
# @Author  : wuwenxi

"""
逻辑运算符
 and : x and y, boolean与, x和y 需要同时满足为 True, x和y 只有一个为 False 表达式为False 等同于java中&&
 or: x or y, boolean 或, x和y只要满足一个为True, 则表达式为True, 等同于java中||
 not: not x, boolean 非, x为True则表达为False, x为False则表达式为True, 等同于java中!
"""

x = 1
y = 2

if x == 2 and y == 1:
    print("x and y: ", (x and y))

if x == 1 or y == 1:
    print("x or y: ", (x or y))

if not (x == 2 and y == 1):
    print("not x: ", x)