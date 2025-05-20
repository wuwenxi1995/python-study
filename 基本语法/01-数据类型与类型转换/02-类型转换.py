# -*- coding: utf-8 -*-
# @Time    : 2025/5/20 09:56
# @Author  : wuwenxi

"""
把一种类型转换成另外一种
int(变量) 将变量转化为整数类型
float(变量) 将变量转化为浮点类型
str(变量) 将变量转化为小数类型
list() 变量转换为数组
tuple() 变量转换为元组
dict() 变量转换为字典
"""
str1 = '9'
num1 = int(str1)
print(num1, type(num1), sep=',')

str2 = '9.'
num2 = float(str2)
print(num2, type(num2), sep=',')

int9 = 9
print(str(int9), type(int9), sep=',')

to_list = list([1, 2, 3])
print(to_list, type(to_list), sep=',')

to_tuple = tuple(('1', '2', 3))
print(to_tuple, type(to_tuple), sep=',')

to_dict = dict(name="TOM", age=20)
print(to_dict, type(to_dict), sep=',')