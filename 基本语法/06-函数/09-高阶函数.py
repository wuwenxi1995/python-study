# -*- coding: utf-8 -*-
# @Time    : 2025/7/29 15:40
# @Author  : wuwenxi

import functools

"""
    op_func 作为传递函数

"""


def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(calc(0, add, 1, 2, 3, 4, 5))  # 15
print(calc(1, mul, 1, 2, 3, 4, 5))  # 120


def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


old_nums = [35, 12, 8, 99, 60, 52]
print(list(map(square, filter(is_even, old_nums))))  # [144, 64, 3600, 2704]

d = dict(zip(
    filter(is_even, old_nums),
    map(square, filter(is_even, old_nums))
))
for k, v in d.items():
    print(k, v)

'''
    lambda表达式改进
'''
d = dict(zip(filter(lambda x: x % 2 == 0, old_nums), map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums))))
for k, v in d.items():
    print(k, v)

'''
    all函数
'''

# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
print(is_prime(37))  # True

"""
    偏函数
"""

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))  # 1001

print(int2('1001'))  # 9
print(int8('1001'))  # 513
print(int16('1001'))  # 4097

"""
 抽象类作为
"""


class Abstract:
    def method_a(self):
        pass

    def method_b(self):
        pass


class A(Abstract):

    def method_a(self):
        print("this is A.method_a")

    def method_b(self):
        print("this is A.method_b")


class B(Abstract):

    def method_a(self):
        print("this is B.method_a")

    def method_b(self):
        raise NotImplemented


class C:
    ...


def method(abstract: Abstract):
    abstract.method_a()
    abstract.method_b()

# method(A())
# method(B())
