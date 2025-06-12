# -*- coding: utf-8 -*-
# @Time    : 2025/6/12 11:41
# @Author  : wuwenxi

'''
属性优先级
'''


class Dog(object):
    count = 1

    def __init__(self, name, age, count):
        self.name = name
        self.age = age
        self.count = count


dog = Dog('xxx', 1, 2)
print("这是实例属性", dog.count)
print("这是类属性", Dog.count)

Dog.count += 1
print("类属性发生变化", Dog.count)
dog.count += 1

