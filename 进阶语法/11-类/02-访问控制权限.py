# -*- coding: utf-8 -*-
# @Time    : 2025/6/12 17:53
# @Author  : wuwenxi

"""

"""


class A:
    def method(self):
        print("this is A public")

    '''
    使用@staticmethod注解为静态方法
    '''

    @staticmethod
    def _method():
        print("this is A protect")

    def __method(self):
        print("this is A private")


class B(A):
    def method(self):
        super().method()
        super()._method()
        # super().__method()


b = B()
print(b.method())
print(b._method())

print("通过类调用静态方法:", A._method())
