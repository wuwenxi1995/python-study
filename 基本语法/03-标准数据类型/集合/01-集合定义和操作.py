# -*- coding: utf-8 -*-
# @Time    : 2025/5/19 22:08
# @Author  : wuwenxi

"""
特性：元素无序不重复,不支持下标操作,
    集合中的元素必须是不可变的（如数字、字符串、元组），不能包含列表、字典等可变类型
定义：使用大括号包含数据
    num = {123, 456, 789}
    set1 = set("123")
    empty = set() # 创建空集合
操作:
    新增：
        add(): 添加元素
        update(): 追加对象必须是可迭代对象,如列表，元组甚至集合，添加字典时只会将key添加到集合中
    删除:
        remove(): 删除指定的值,如果不存在则报错
        discard(): 删除指定的值
        pop(): 随机删除某个元素, 如果集合为空 则报错
    交集:
        使用&符号取两个集合的交集
        intersection():　取两个集合的交集，结果返回一个新的集合
    并集:
        使用|符号取两个集合的并集
        union(): 合并两个集合, 结果返回一个新的集合
    差集：
        使用-符号取两个集合的差集
        difference(): 取两个集合的差集, 结果返回一个新的集合
    对称差集:
        使用^符号取两个集合的补集
        symmetric_difference()：取两个集合的对称差集, 结果返回一个新的集合
    集合间判断
        issubset(set): 集合是否为set集合的子集
        issuperset(set): 集合是否为set集合的超集
        isdisjoint(set): 集合是否与set集合有交集

"""
num = {123, 456, 789}
set1 = set("123")
empty = set()

num.add(321)
print("add num:", num)

num.update([432, 12])
print("update num:", num)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("a&b", a & b)
new_a = a.intersection(b)
print('intersection', new_a)

print("a|b", a | b)
new_a = a.union(b)
print('union', new_a)

print("a-b", a - b)
new_a = a.difference(b)
print('difference', new_a)

print("a^b", a ^ b)
new_a = a.symmetric_difference(b)
print('symmetric_difference', new_a)
