# -*- coding: utf-8 -*-
# @Time    : 2025/6/13 16:05
# @Author  : wuwenxi

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius  # 实例属性
        self.ingredients = ingredients

    # 实例方法：计算面积
    def area(self):
        return self.circle_area(self.radius)  # 调用静态方法

    # 类方法：创建固定尺寸的披萨
    @classmethod
    def margherita(cls):
        return cls(12, ["mozzarella", "tomatoes"])  # 调用__init__

    # 类方法：创建另一种固定尺寸的披萨
    @classmethod
    def prosciutto(cls):
        return cls(16, ["mozzarella", "tomatoes", "ham"])

    # 静态方法：计算圆面积（工具函数）
    @staticmethod
    def circle_area(r):
        return r ** 2 * 3.14159


# 使用示例
p1 = Pizza.margherita()  # 通过类方法创建实例
p2 = Pizza.prosciutto()
print(p1.area())  # 调用实例方法
print(Pizza.circle_area(5))  # 调用静态方法
