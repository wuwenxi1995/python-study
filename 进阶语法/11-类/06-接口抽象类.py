# -*- coding: utf-8 -*-
# @Time    : 2025/6/17 22:12
# @Author  : wuwenxi

"""
    接口/抽象基类
"""

from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self): pass


class Movable(ABC):
    @abstractmethod
    def move(self): pass


class Sprite(Drawable, Movable):
    def draw(self):
        print("Drawing sprite")

    def move(self):
        print("Moving sprite")
