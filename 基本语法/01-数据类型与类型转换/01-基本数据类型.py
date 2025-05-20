# -*- coding: utf-8 -*-
# @Time    : 2025/5/20 10:01
# @Author  : wuwenxi

r"""
python提供的标准数据类型
    Number类型：int、float、complex(复数)
    布尔类型: True/False
    Str：字符串
    List：列表
    Tuple: 元组
    Set: 集合
    Dict: 字典

1. 数字类型的数学运算
    1.1 运算符 +, -, * 和 / 按照数学中计算规则进行先后处理
    1.2 除法运算 (/) 总是返回浮点数, 得到整数可以使用(//) 向下取整, 使用%求余
    1.3 用 ** 运算符计算乘方
        5 ** 2 -> 输出：25
    1.4 使用=进行赋值操作, == 比较两个值
    1.5 混合类型运算数的运算会把整数转换为浮点数
        4 * 3.75 - 1 -> 输出：14.0
    1.6 除了支持int和float类型, 还支持 Decimal(金额)或 Fraction(有理数). Python 还内置支持 复数，后缀 j 或 J 用于表示虚数（例如 3+5j）
        创建有理数
            from fractions import Fraction
            from decimal import d
            # 整数创建
            f1 = Fraction(1,3) -> 输出: 1/3
            # 字符串创建
            f2 = Fraction('1/3') -> 输出: 1/3
            # 浮点数创建
            f3 = Fraction(0.75) -> 输出：3/4
            f4 = Fraction(0.8).limit_denominator() -> 使用limit_denominator函数简化输出: 4/5
            # 从小数或分数创建
            f5 = Fraction(d('0.5')) -> 输出：1/2
            f6 = Fraction(1,2)
            f7 = Fraction(f6) -> 输出：1/2
            # 获取分子分母
            f = Fraction(3, 4)
            print(f.numerator) -> 输出: 3
            print(f.denominator) -> 输出: 4
        复数
            # 直接赋值
            c = 3 + 4j
            print(c.numerator, c.denominator)
            # 使用complex()函数
            c1 = complex(3,4) -> 创建3+4j的复数
            c2 = complex(3) -> 创建3+0j的复数
            c3 = complex('3+4j') -> 从字符串创建
            # Python支持对复数进行基本的算术运算，包括加法、减法、乘法、除法等。此外，还支持幂运算和共轭操作
2. 字符串
    2.1 使用\进行字符串转义，如标示字符串中本身的引号，如果不希望前置\被解释为转义字符, 可以在字符串前加上r
        print('C:\software\name') -> 输出：C:\software
        print(r'C:\software\name') -> 输出：C:\software\name
    2.2 字符串中的format, 在字符串前使用f
        a = 'abc'
        print(f'This string is {a}')
    2.3 字符串拼接, 使用+直接拼接两个字符串, 可以使用* 重复字符串, 也可以将字符串用空格隔开进行连接(仅限于字符串子字面值,
    不能使用定义变量或表达式), 如果要将变量和字面值拼接只能用+
        p = 'Pyth' + 'on' -> 输出:Python
        p1 = 'Pyth' 'on' -> 输出:Python
        p2 = 'num' * 2 + 1 -> 输出: numnum1
    2.4 支持索引访问, 用负数索引时，从右边开始计数, 和java一样存在数组越界
        w = ‘Python’
        print(w[0]) -> 输出：P
        print(w[5]) -> 输出：n
        print(w[-1]) -> 输出倒数第一个字符：n
        print(w[-6]) -> 输出最后一个：P
        print(w[6],w[-7]) -> 数组越界
    2.5 支持切片(字符串截取), 输出结果包含切片开始，但不包含切片结束; 切片能自动处理数组越界
        w = 'Python'
        print(w[0,2]) -> 输出: Py
        print(w[2,6]) -> 输出：thon
        print(w[:3]) -> 输出[0,3]位置的字符串 -> Pyt
        print(w[3:]) -> 输出[3,结束位置]的字符串 -> hon
        print(w[-2:]) -> 输出倒数第二个字符到末尾的字符串 -> on

        print(w[:2]+w[2:]) -> 输出:Python

        print(w[3,10]) -> 输出: hon
        print(w[10:]) -> 输出：''
    2.6 字符串不允许修改
        w = 'Python'
        w[0] = 'J' -> 非法操作
        w[2:] = 'py' -> 非法操作
        # 正确的方法 重新生成字符串
        print('p' + w[1:]) -> 输出：python
"""
# 使用type()函数打印数据类型

# 整数类型
a = 11
# 浮点类型
b = 3.1415926
# 字符串类型
c = 'python'

print(a, b, c)
print(type(a), type(b), type(c))