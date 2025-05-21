# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 15:50
# @Author  : wuwenxi

def fun():
    global a  # 将变量a申明为全局变量
    a = 200  # 修改变量a
    print('a:', a)


def funb():
    print('a:', a)


a = 100
fun()  # 输出 200
funb()  # 输出 200 如果在fun中不将a设为全局变量则 输出100


# def fun():
#     print('a:', a)  # 引用了未定义的变量, a并没有申明是全局变量
#     a = 2
#
#
# fun()

