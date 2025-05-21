# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 17:06
# @Author  : wuwenxi

"""
函数定义: 函数名 = lambda 形参:返回值
"""


def fun(a, b):
    return a + b


print(fun(1, 2))

# 使用匿名函数
fun = lambda a, b: a + b
print(fun(1, 2))


def inc(n):
    return lambda x: x + n


'''
可以理解为 f 是一个新函数
 def f(x):
    return 10 + x
'''
f = inc(10)

print(f(1))

'''
结合三目运算
'''

f = lambda a, b: a + b if a > b else a
print(f(3, 2))
