"""
1. for循环基本语法

for 临时变量 in 数据容器(列表、元组、字典、集合):
    满足条件执行的代码

2. range函数 可以生成一个等差数列, 生成的序列不包括给定的终止值

3. 跳出循环 break/continue

4. 循环的else子句
在 for 或 while 循环中 break 语句可能对应一个 else 子句。 如果循环在未执行 break 的情况下结束, else 子句将会执行。

5. match语法: 类似java中的switch, 但功能更为强大，因为它不仅支持简单的值匹配，还可以处理复杂的对象和数据结构
    match 变量:
        case: x1
        case: x2
        case: x3
        # 通配符 并必定会匹配成功
        case: _
          break
    5.1 匹配字面量(如字符串、数字)
    5.2 匹配常量，使用枚举
        from enum import Enum

        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3
        color = Color.RED
        match color:
            case Color.RED:
                print("The color is red.")
            case Color.GREEN:
                print("The color is green.")
            case Color.BLUE:
                print("The color is blue.")
    5.3 匹配序列(如列表、元组)
        point = (1, 2)

        match point:
            case (0, 0):
                print("Origin")
            case (0, y):
                print(f"Y-axis at {y}")
            case (x, 0):
                print(f"X-axis at {x}")
            case (x, y):
                print(f"Point at ({x}, {y})") -> 输出当前内容
            case _:
                print("Not a point")
    5.4 匹配字典, case语句中只要能匹配上字典中对key即可匹配成功
        person = {"name": "Alice", "age": 30}

        match person:
            case {"name": name, "age": age}:
                print(f"Name: {name}, Age: {age}")
            case _:
                print("Invalid person data")
    5.5 使用守卫进一步限制匹配规则,使用if作为守卫子句。如果守卫子句的值为假，那么 match 会继续尝试匹配下一个 case 块
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Point(1, 2)
        match p:
            case Point(x, y) if x == y:
                print(f"Y=X at {x}")
            case Point(x, y):
                print(f"Not on the diagonal")
    5.6 捕获绑定，用名称来捕获绑定对值
        match point:
            case (x, y):
                print(f"Captured x={x}, y={y}")
    5.7 类匹配
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Point(1, 2)

        match p:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else") -> 输出当前内容
            case _:
                print("Not a point")

    5.8 OR模式匹配
        status = 404

        match status:
            case 200 | 201:
                print("Success")
            case 400 | 404:
                print("Client error")
            case 500 | 502 | 503 | 504:
                print("Server error")
            case _:
                print("Unknown status")
    5.9 使用as关键字捕获整个值
        data = [1, 2, 3]

        match data:
            case [first, *rest] as full_list:
                print(f"First element: {first}, Rest: {rest}, Full list: {full_list}")

"""
c = range(10)

for item in c:
    print(item)

# range 可以不从 0 开始，且可以按给定的步长递增, 即使是负数步长
print(list(range(2, 10, 3)))

# 按索引迭代序列
a = ['Tom', 'Jack', 'James', 'Mac']
for i in range(len(a)):
    print(i, a[i])

# 格式化输出
for item in range(1, 6):
    print(f'正在输出{item}')

#  while/if/elseif/else 语法
while True:
    x = int(input("Please enter an integer: "))
    if x < 0:
        print("Negative changed to zero, break")
        break
    elif x == 0:
        print("Zero")
    # 范围取值
    elif 10 >= x >= 1:
        print("1 - 10")
    else:
        print("More than 10")

# 循环中的else子句
'''
在 for 循环中, else 子句会在循环结束其他最后一次迭代之后，即未执行 break 的情况下被执行。
在 while 循环中，它会在循环条件变为假值后执行。
在这两类循环中，当在循环被 break 终结时 else 子句 不会 被执行。 当然，其他提前结束循环的方式，如 return 或是引发异常，也会跳过 else 子句的执行。
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # 循环到底未找到一个因数
        print(n, 'is a prime number')

# while循环里面else子句
search_list = [1, 2, 3, 4, 5]
target = 6
index = 0

while index < len(search_list):
    if search_list[index] == target:
        print(f"Target {target} found at index {index}.")
        break
    index += 1
else:
    print(f"Target {target} not found in the list.")
