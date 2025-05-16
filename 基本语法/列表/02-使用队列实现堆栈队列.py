# -*- coding: utf-8 -*-
# @Time    : 2025/5/16 15:43
# @Author  : wuwenxi

from collections import deque

"""
堆栈
    1. 使用append()和pop()实现先进后出的栈
    2. 使用collections.deque实现栈
队列
    1. 使用append()和pop(0)实现先进先出的队列; 列表作为队列的效率很低。因为，在列表末尾添加和删除元素非常快，
            但在列表开头插入或移除元素却很慢
    2. 优先使用collections.deque 实现队列
    
deque 在for循环中不允许修改操作元素

"""

# 栈
stack = [1, 2, 4]
stack.append(5)
stack.append(6)
print(stack)

while stack.__len__() > 0:
    print(stack.pop())

stack2 = deque([3, 2, 1])
print("stack2:", stack2)
stack2.append(5)
print("stack2 after append :", stack2)

# deque 在for循环中不允许修改元素
# for i in stack2:
#   print(stack2.pop())

while stack2.__len__() > 0:
    print("stack2.pop :", stack2.pop())

# 队列
queue = deque([1, 2, 3])
print('queue:', queue)
queue.append(4)
queue.append(5)
print('queue after append:', queue)

print(queue.popleft())
print('after popleft:', queue)
