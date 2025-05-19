# -*- coding: utf-8 -*-
# @Time    : 2025/5/18 16:57
# @Author  : wuwenxi

"""
定义：元组是由多个用逗号隔开的值组成定义元组时, 可以不使用圆括号，但在输出时必定包含圆括号，这样才能正确地解释嵌套元组；
     元组是[不可以对象]即，定义后元组内元素不允许修改, 但元素可以是可变对象；如元素可以是列表
     元组是可以由不同类型的元素组成，列表一般情况下为相同类型的元素组成，元组一般通过解包或者索引访问，列表可以通过迭代器遍历；
     构造0或1个元素的元组：空圆括号就可以创建空元组，一个元素的元组可以通过在这个元素后添加逗号来构建（圆括号里只有一个值的话不够明确）

特性：元组的不可修改和删除特性可以提高代码安全性，

操作：不允许修改, 只允许查找
    下标查找：
    index(): 查找元素是否在元组存在，不存在抛出异常; 存在返回下标索引
    count(): 统计元素在元组中出现的次数
"""

fruits = 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'
print(fruits[1])

# 嵌套元组
t = fruits, (1, 2, 3, 4)
print('嵌套元组', t)
# 输出 ==> (('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'), (1, 2, 3, 4))

# 不可变对象
try:
    fruits[1] = 'apple1'
except TypeError as e:
    print("操作错误:", e)
    # TypeError: 'tuple' object does not support item assignment
# 元素可以包含可变对象
v = ([1, 2, 3], [3, 2, 1])
print('有可变元素对象的元组', v)
v[0][2] = 4
print('修改后的元组', v)

# 空元组
empty = ()

# 一个元素的元组
# 如果定义为 single = ('apple') 与字符串类型由歧义 因此必须在元素后加上逗号来明确定义类型为元组
single = ('apple',)
print(single.__len__())

# 访问元素 也可以称为解包
t = v[0]
x, y, z = t
print(x, y, z)
