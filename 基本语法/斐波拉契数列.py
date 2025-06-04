# -*- coding: utf-8 -*-
# @Time    : 2025/6/4 23:26
# @Author  : wuwenxi

"""
求斐波拉契数列第n项的值 1,1,2,3,5,8,13,21

"""


def funa(n):
    if n <= 2:
        return 1
    elif n <= 3:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, n):
            tem = b
            b = a + b
            a = tem
        return b


def funb(n):
    if n <= 2:
        return 1
    elif n <= 3:
        return 2
    else:
        return funb(n - 1) + funa(n - 2)


print(funa(2))
print(funa(4))
print(funa(7))
