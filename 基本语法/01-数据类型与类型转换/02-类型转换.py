# -*- coding: utf-8 -*-
# @Time    : 2025/5/20 09:56
# @Author  : wuwenxi

"""
把一种类型转换成另外一种 使用type() 可以检查数据类型
    int(变量) 将变量转化为整数类型
    float(变量) 将变量转化为浮点类型
    str(变量) 将变量转化为小数类型
    list(变量) 变量转换为列表
    tuple(变量) 变量转换为元组
    dict(变量) 变量转换为字典
    set(变量) 变量转换为集合
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

# 使用tuple转为元组
l = [1, 2, 3]
# 将列表 转为元组
print("list to tuple, ", tuple(l))
to_tuple = tuple(('1', '2', 3))
print(to_tuple, type(to_tuple), sep=',')

# 使用set转为集合
s = [1, 2, 3, 3]
print("list to set ", set(s), sep=':')

# 使用dict转换字典
a = ['a1', 'b1', 'c1', 'c2']
b = ['a2', 'b2', 'c2', 'c3']
# 使用zip将a、b列表进行打包绑定, 再转换为字典
print('to dict', dict(zip(a, b)))
# 直接绑定变量名
to_dict = dict(name="TOM", age=20)
print(to_dict, type(to_dict), sep=',')
