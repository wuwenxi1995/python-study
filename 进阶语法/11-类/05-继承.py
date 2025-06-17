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


"""
    同名方法调用规则
"""


class A:
    def method(self):
        return "A"


class B(A):
    def method(self):
        return f"B -> {super().method()}"


class B2(A):
    def method(self):
        return "B"


class C(A):
    def method(self):
        return f"C -> {super().method()}"


class D1(B2, C):
    pass


class D2(B, C):
    def method(self):
        return C.method(self)


class D3(B, C):
    def method(self):
        return f"D -> {super().method()}"


# MRO 直接调用method
md1 = D1()
print("MRO 直接调用method: ", md1.method())

# 手动指定调用父类方法
md2 = D2()
print("手动指定调用父类方法: ", md2.method())

# 使用super调用方法
md3 = D3()
print("使用super以此调用方法: ", md3.method())  # 输出: D -> B -> C -> A（A的method只被调用一次）
