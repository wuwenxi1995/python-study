"""
支持索引访问, 用负数索引时，从右边开始计数, 和java一样存在数组越界
        w = ‘Python’
        print(w[0]) -> 输出：P
        print(w[5]) -> 输出：n
        print(w[-1]) -> 输出倒数第一个字符：n
        print(w[-6]) -> 输出最后一个：P
        print(w[6],w[-7]) -> 数组越界
支持切片(字符串截取), 输出结果包含切片开始，但不包含切片结束; 切片能自动处理数组越界
        w = 'Python'
        print(w[0,2]) -> 输出: Py
        print(w[2,6]) -> 输出：thon
        print(w[:3]) -> 输出[0,3]位置的字符串 -> Pyt
        print(w[3:]) -> 输出[3,结束位置]的字符串 -> hon
        print(w[-2:]) -> 输出倒数第二个字符到末尾的字符串 -> on

        print(w[:2]+w[2:]) -> 输出:Python

        print(w[3,10]) -> 输出: hon
        print(w[10:]) -> 输出：''
"""

contains = "abcsfds".find('fd')
print(contains)