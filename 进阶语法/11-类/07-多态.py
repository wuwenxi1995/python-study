# -*- coding: utf-8 -*-
# @Time    : 2025/6/17 22:32
# @Author  : wuwenxi

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who(self):
        return 'I am a Person, my name is %s' % self.name


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def who(self):
        return 'I am a Student, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def who(self):
        return 'I am a Teacher, my name is %s' % self.name


class Worker(Person):
    def __init__(self, name, age, work):
        super().__init__(name, age)
        self.work = work


p = Person('Tom', 20)
s = Student('Mark', 22, 100)
t = Teacher('John', 26, 90)
w = Worker('Jack', 40, 'cleaner')
print(p.who())
print(s.who())
print(t.who())
print(w.who())

"""
使用isinstance检测对象类型
"""
print(isinstance(p, Person))
print(isinstance(s, Person))
print(isinstance(s, Student))
print(isinstance(s, Teacher))


