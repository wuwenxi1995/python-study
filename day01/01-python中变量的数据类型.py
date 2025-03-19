# coding:UTF-8
r"""
python中共有7种基本数据类型
数字类型(整数int、浮点类型float)
布尔类型 True/False
字符串类型 str
列表类型
元组类型
字典类型
集合类型

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
3. 列表
    3.1 可以包含不同类型的元素，但一般情况下，各个元素的类型相同
    3.2 支持索引和切片
        s = [1, 4, 9, 16, 25, 36]
        print(s[2]) -> 输出：4
        print(s[-2]) -> 输出：25
        print(s[-2:]) -> 输出：[25, 36]
    3.3 支持合并
        s1 = [1, 4, 9, 16, 25, 36]
        s2 = [49, 64, 81, 100]
        print(s1 + s2)
    3.4 列表可以修改，可以直接根据索引下标或append()修改添加元素
         s = [1, 4, 9, 17, 25, 36]
         s[3] = 16
         print(s) -> 输出: [1, 4, 9, 16, 25, 36]
         s.append(49) -> 输出: [1, 4, 9, 16, 25, 36, 49]
    3.5 列表赋值, 将列表赋值给一个变量时, 该变量将引用列表, 当列表中的值发生修改时, 引用该列表的所有变量都见看到
        rgb = ['red', 'green', 'blue']
        rgba = rgb -> rgba、rgb都引用了['red', 'green', 'blue']列表
        print(id(rgb) == id(rgba)) -> 输出：True 指向同一个列表
        rgba.append('black')
        print(rgb) -> 输出：['red', 'green', 'blue', 'black']
    3.6 切片后的列表为新列表, 切片操作属于是浅拷贝, 切片赋值可以改变列表大小
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
    3.7 len()函数返回列表长度
    3.8 多维列表(java中的多维数组)
        a = [1,2,3]
        b = [3,4,5]
        x = [a,b]
        print(x) -> [[1,2,3],[3,4,5]]
        print(x[1]) -> [3,4,5]
        print(x[0][1]) -> 2
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
