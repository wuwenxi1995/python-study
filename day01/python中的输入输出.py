"""
1. 输出使用print()函数
2. 输入使用input()函数
    2.1 阻塞当前线程等待用户输入
    2.2 输入值永远都是str
"""

# context = input("请输入内容:")
# print(type(context), context)
#
# # 将输出内容连接起来
# # print(输出内容, sep="", end="") sep输入内容按什么连接 ,end以什么结尾
# print(type(context), context, sep=',', end='.')


person = {"name": "Alice", "age": 30}

match person:
    case {"age": name}:
        print(f"Name: {name}")
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")
    case _:
        print("Invalid person data")
