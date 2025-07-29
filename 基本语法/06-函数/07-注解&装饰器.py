# -*- coding: utf-8 -*-
# @Time    : 2025/7/28 22:16
# @Author  : wuwenxi

def decorator(planes):
    def func(fn):
        fn.planes = planes
        return fn

    return func


@decorator(1)
def one():
    print('this is one')


@decorator(2)
def two():
    print('this is two')


default = [
    one,
    two
]

for f in default:
    print(f.planes)
    f()

