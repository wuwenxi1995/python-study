# -*- coding: utf-8 -*-
# @Time    : 2025/5/16 17:12
# @Author  : wuwenxi

from math import pi

"""
1. 列表推导式
    定义: 简化列表定义, 对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表; 或用满足特定条件的元素创建子序列
    函数定义: list = [表达式 for . in . if .]; 一个表达式, 后面可以有0个或多个for in或多个if子句; 
        生成的新列表是由表达式依据for和if子句计算得出的; 注意如果表达式是元组、列表、字典、集合必须加上对应符号
    总结: 使用列表推导式更简洁, 易读
        
    例1: 创建平方值的列表
        常规创建方法:
            squares = []
            for i in range(10):
                squares.append(i**2)
        列表推导式:
            squares = [x**2 for x in range(10)]
        
    列2: 将两个列表不相等元素组合成新列表
        常规创建方法:
            combs = []
            for x in [1,2,3]:     
                for y in [3,1,4]:
                    if x != y:
                        combs.append((x,y))
        列表推导式:
            combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
    列3: 展平嵌套列表
        vec = [[1,2,3], [4,5,6], [7,8,9]]
        vec_new = [x for inner in vec for num in inner]
2. 嵌套列表推导式

"""

combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
combs2 = [[x, y] for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
combs3 = [{x, y} for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print(f'combs:{combs}, combs2:{combs2},combs3:{combs3}')

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec_new = [num for inner in vec for num in inner]
print(vec_new)
