# -*- coding: utf-8 -*-
# @Time    : 2025/5/20 10:10
# @Author  : wuwenxi

"""
浅拷贝：创建一个新对象，将原始对象中的元素引用添加到新对象中，如果这些元素是可变元素(非基本类型, 如列表、字典),
       当在一个对象中对可变元素进行修改时，将影响所有引用该可变元素的对象。python中可以使用copy.copy()进行
       浅拷贝
深拷贝：创建一个新对象，将元素对象中所有可变元素都重新创建新的元素并引用到新对象当中，新对象和原始对象是完全独立
       的修改深拷贝后的对象不会影响原对象。python中可以使用copy.deepcopy()进行深拷贝

rgb = ['red', 'green', 'blue']
rgba = rgb[:]
rgba[-1] = 'bluea'
print(rgb) -> 输出: ['red', 'green', 'blue'] -> 字符串是不可变元素, 不影响原列表
print(rgba) -> 输出: ['red', 'green', 'bluea']

list = [[1,2,3], [4,5,6]]
copy_list = list[:]
copy_list[0][0] = 'change'
print(list) -> 输出: [['change',2,3], [4,5,6]] —> list中的元素是可变元素, 对可变元素修改, 影响原列表

切片操作属于是浅拷贝, 切片赋值可以改变列表大小

"""
