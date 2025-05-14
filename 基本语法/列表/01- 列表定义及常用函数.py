# -*- coding: utf-8 -*-
# @Time    : 2025/5/14 22:06
# @Author  : wuwenxi

"""
List:列表 => [10,20,30] ['Tom','Jack','James']
特性: 有序集合, 元素类型可以不同类型类似java中存储obj对象

列表基本操作:
    添加元素：append(obj) 在列表末尾添加一个元素; extend(obj) 将另一个列表添加到当前列表的末尾
            insert(index,obj) 在指定位置前插入元素; 添加元素时如果是元组可以将元组对象加入到列表中
    count(x): 统计列表中元素 x 出现的次数
    pop([i]): 删除列表中指定位置的元素，并返回被删除的元素; 如果未指定 i 则移除末尾的元素
    copy(): 浅拷贝
    index(x, start, end): 元素 x 在列表中的位置, 如果列表不包含元素x抛出异常; 可选参数
            start, end 指定查询在元素x 在[start, end]范围内的子序列中的位置
    reverse(): 反转列表
    sort(*, key=None, reverse=False): 列表排序, key指定排序规则的函数; reverse一个
            布尔值。若设置为 True，则列表会按照降序排列；若为 False（默认），则按升序排列
            与 sorted() 函数的区别：
            sort() 方法是列表对象的一个方法，它会直接修改原列表；而 sorted() 是一个内置
            函数，它会返回一个新的排序后的列表，原列表保持不变
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("apple count: ", fruits.count("apple"))

f = ('water1', 'water2')
fruits.insert(2, f)
print('insert: ', fruits)
# 输出: ==>  ['orange', 'apple', ('water1', 'water2'), 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.append(f)
print('append: ', fruits)

#　输出: ==> ['orange', 'apple', ('water1', 'water2'), 'pear', 'banana', 'kiwi', 'apple', 'banana', ('water1', 'water2')]

copy = fruits.copy()
copy.extend(fruits)
print("expend: ", copy)
print("fruits contains: ", fruits.__contains__("tom"))

'''
 排序
'''
# 按照值长度降序排序
fruits.sort(key=len, reverse=True)
print("sort: ", fruits)

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 22}
]

sorted_student = sorted(students, key=lambda sort: sort["age"], reverse=True)
print(f"sorted_student: {sorted_student}, students: {students}")
students.sort(key=lambda sort: sort["age"], reverse=True)
print("students: ", students)
