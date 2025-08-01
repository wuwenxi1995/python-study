# -*- coding: utf-8 -*-
# @Time    : 2025/8/1 16:03
# @Author  : wuwenxi

import collections as c

'''
    适用于对象存储
'''


class Person(c.namedtuple('Person', 'name age gender addr work')):

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age}, gender={self.gender}, addr={self.addr}, work={self.work})'


p = Person(18, '张三', '男', '上海', 'cxy')
print(p)
