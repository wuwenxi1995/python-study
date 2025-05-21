# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 16:42
# @Author  : wuwenxi

a = 10


def fun():
    a = 1

    def funb():
        nonlocal a
        print('funb a:', a)
        a += 1

    funb()
    print('fun a:', a)


fun()
print(a)
