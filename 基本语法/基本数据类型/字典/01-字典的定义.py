# -*- coding: utf-8 -*-
# @Time    : 2025/5/19 21:41
# @Author  : wuwenxi

"""
字典特性: 键值对存储,key不允许重复, python3.6之前的版本字典是无序的, python3.6可以依赖Cpython实现有序
        3.7之后字典在python语言规范中定义为有序;
            遍历时按插入顺序返回元素;
            更新键值不会改变元素顺序（除非删除后重新插入）;
            合并字典（如 d1 | d2）保留合并顺序;
        数据结构类似java中LinkedHashMap, 底层数据结构为哈希表
定义：
    使用一对大括号定义数据 dict = {"key1":"value1", "key2":"value2"}
    使用dict1 = dict({"":""})

常用操作：
    新增/更新: 存在则覆盖更新, 不存在则新增元素
        people = dict({"name": "Tom", "age": 30, "gender": "male"})
        people['id'] = 110
        people['name'] = 'wuwenxi'
        ==> 输出：{'name': 'wuwenxi', 'age': 30, 'gender': 'male', 'id': 110}
       update(): 追加可迭代对象
    删除：
        del语句
            del people['gender']
        pop(obj): 删除指定键, 如果不存在key则抛出异常
        popitem(): 从字典末端移除键值
        clear(): 清空字典
    查询：
        people = dict({"name": "Tom", "age": 30, "gender": "male"})
            print(people['age']) ==> 输出:30
        keys(): 查看所有键信息
        values(): 查看所有值信息
        get(obj): 根据键查询值信息, 不存在返回None
        items(): 输出字典键值, 与java中foreach类似
            for k,v in people.items():
                print(k, v)
        setdefault("key","default_value"): 查询key,如果存在key则返回value，否则不存在key则返回default_value
"""

people = dict({"name": "Tom", "age": 30, "gender": "male"})
people['id'] = 110
print('dict add: ', people)
people['name'] = 'wuwenxi'
print('dict modify: ', people)

people.update({"work": "IT", "company": "SH"})
print('dict update: ', people)

value = people.setdefault("school", "CCT")
print(f"setdefault:{value}, people:{people}")

i = 0
while i < 2:
    value = people.popitem()
    print(f'dict popitem value: {value}, people:', people)
    i += 1

print(people.keys())
print(people.values())

print(people.get("null"))
print(people.__contains__("age"))
for k, v in people.items():
    print(k, v)

people.clear()
