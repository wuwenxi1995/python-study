# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 21:04
# @Author  : wuwenxi

import builtins
import functools
from functools import reduce

"""
python中已经内置的函数，可以直接调用, 使用dir函数可以查看内置函数
"""

print(dir(builtins))

print(abs(-3))  # abs()函数取绝对值
# 　求最大值最小值
print(min([1, 2, 3]))
print(max([1, 2, 3]))

'''
将可迭代对象打包成一个一个元组 并返回元组内容
如果变量元素个数不一致时 按最少个数进行打包
'''
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
c = [1, 2, 3, 4, 5, 6, 7, 8]

for i in zip(a, b, c):
    print(i)  # ==> 输出：(1, 4, 1),(2, 5, 2),(3, 6, 3)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
print(list(zip(*matrix)))  # ==> 输出:[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

'''
 map(function, iterable)
 将可迭代对象的每一个元素都分别进行映射，分别执行function
'''
# 计算列表元素的平方, 并返回新列表
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# 对参数序列中元素不断减少
'''
reduce(func, iterable, initial=_initial_missing)
对可迭代对象进行累加减乘除, 最终得到一个值
'''

print(functools.reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 1))
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 0))
print(reduce(lambda x, y: x - y, [1, 2, 3, 4, 5], 0))

'''
enumerate枚举, 用与将一个可迭代对象组合为一个索引序列，同时列出数据和数据下标 一般用于for循环
enumerate(iterable, start=0): iterable 可迭代对象, start 起始迭代位置
'''
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 22}]
for i, v in enumerate(students, 1):
    print(i, students[i - 1])

print(list(enumerate(students))) # ==> 输出: [(0, {'name': 'Alice', 'age': 20}), (1, {'name': 'Bob', 'age': 18}), (2, {'name': 'Charlie', 'age': 22})]
print(dict(enumerate(students))) # ==> 输出: {0: {'name': 'Alice', 'age': 20}, 1: {'name': 'Bob', 'age': 18}, 2: {'name': 'Charlie', 'age': 22}}
