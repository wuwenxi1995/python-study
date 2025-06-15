# -*- coding: utf-8 -*-
# @Time    : 2025/6/13 16:33
# @Author  : wuwenxi

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender


p = Person("Tom", 32)
s = Student("Tomas", 15, "male")

print('name:{}, age:{}'.format(p.name, p.age))
print('student name:{}, age:{}, gender:{}'.format(s.name, s.age, s.gender))

"""
     多继承

"""


class A:
    def __init__(self):
        print("A's __init__")


class B(A):
    def __init__(self):
        super().__init__()  # 调用A的__init__
        print("B's __init__")


class C(A):
    def __init__(self):
        super().__init__()  # 调用A的__init__
        print("C's __init__")


class D(B, C):  # MRO: D -> B -> C -> A
    def __init__(self):
        super().__init__()  # 调用B的__init__
        print("D's __init__")


d = D()
# 输出:
# A's __init__
# C's __init__
# B's __init__
# D's __init__

