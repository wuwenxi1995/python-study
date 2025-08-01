# -*- coding: utf-8 -*-
# @Time    : 2025/8/1 09:34
# @Author  : wuwenxi

import os

os.path.join("..")

'''
    读文件
'''
file = open('../../readme.txt', 'r', encoding='utf-8')
print(file.read())
# for line in file.readlines():
#     print(line)
file.close()

'''
    写文件
'''
write = open('../../write.txt', 'w+', encoding='utf-8')
# write = open('../../write.txt', 'a+', encoding='utf-8')
if write.writable():
    write.write('\nhello world')
if write.readable():
    # 必须移动指针从头开始读，否则会从当前位置末尾开始读
    write.seek(0)
    print(write.read())
write.close()

'''
    上下文管理
'''

print("=" * 20)

try:
    with open('../../write1.txt', 'r', encoding='utf-8') as r:
        print(r.read())
except FileNotFoundError as fnfe:
    print("write1.txt文件不存在")

with open('../../write.txt', 'a+', encoding='utf-8') as w:
    w.write('\nhello world')
    w.seek(0)
    print(w.read())

