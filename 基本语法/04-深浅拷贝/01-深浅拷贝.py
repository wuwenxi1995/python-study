# -*- coding: utf-8 -*-
# @Time    : 2025/5/20 10:10
# @Author  : wuwenxi

import copy as c

"""
变量引用：不同变量引用同一个值时, 这两个变量的引用地址是一致的
        如：a = 10
            b = 10
            print(id(a) == id(b)) ==> 输出：True

浅拷贝：创建一个新对象，将原始对象中的元素引用添加到新对象中，如果这些元素是可变元素(非基本类型, 如列表、字典),
       当在一个对象中对可变元素进行修改时，将影响所有引用该可变元素的对象。python中可以使用copy.copy()进行
       浅拷贝
深拷贝：创建一个新对象，将元素对象中所有可变元素都重新创建新的元素并引用到新对象当中，新对象和原始对象是完全独立
       的修改深拷贝后的对象不会影响原对象。python中可以使用copy.deepcopy()进行深拷贝
       
使用id()查看对象地址信息
切片操作属于是浅拷贝, 切片赋值可以改变列表大小

rgb = ['red', 'green', 'blue']
rgba = rgb[:]
rgba[-1] = 'bluea'
print(rgb) -> 输出: ['red', 'green', 'blue'] -> 字符串是不可变元素, 不影响原列表
print(rgba) -> 输出: ['red', 'green', 'bluea']

list = [[1,2,3], [4,5,6]]
copy_list = list[:]
copy_list[0][0] = 'change'
print(list) -> 输出: [['change',2,3], [4,5,6]] —> list中的元素是可变元素, 对可变元素修改, 影响原列表
"""

# 引用变量, 值共用同一个内存地址
a = 10
b = 10
print(id(a) == id(b))

# 浅拷贝
a = [1, 2, 3, 4]
# 创建新的对象, 内存地址发生改变
b = c.copy(a)

print(f'a, id:{id(a)}, copy b,id:{id(b)}')

# a列表中元素均为不可变元素  因此修改b不影响a
b[2] = -3
print(f'update b, a:{a},b:{b}')

a1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
b1 = c.copy(a1)
print(f'列表中元素为可变对象, a1:{a1},b1:{b1}')
b1[0][2] = -3
print(f'修改b1, a1:{a1},b1{b1}')  # ==> 输出结果中a1 b1均发生改变

# 深拷贝
d = c.deepcopy(a)
print(f'a, id:{id(a)}, deepcopy d,id:{id(d)}')

d1 = c.deepcopy(a1)
print(f'deepcopy ,a1:{a1},d1:{d1}')

d1[0][2] = 2

print(f'update d1, a1:{a1},d1:{d1}')  # ==> 输出结果中,只有d1发生修改
