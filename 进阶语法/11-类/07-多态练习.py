# -*- coding: utf-8 -*-
# @Time    : 2025/6/17 22:52
# @Author  : wuwenxi


# Enter a code
class SkillMixin:
    def skill(self):
        pass


class BasketballMixin(SkillMixin):
    def skill(self):
        print('我会打篮球')


class FootballMixin(SkillMixin):
    def skill(self):
        print('我会踢足球')


class Person:
    def who(self):
        pass


class Student(Person):

    def __init__(self):
        self.skill = BasketballMixin()

    def who(self):
        print('我是学生')
        return self


class Teacher(Person, FootballMixin):

    def __init__(self):
        self.skill = FootballMixin()

    def who(self):
        print('我是老师')
        return self


s = Student()
s.who().skill.skill()

t = Teacher()
t.who().skill.skill()
