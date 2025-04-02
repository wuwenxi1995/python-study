"""
把一种类型转换成另外一种
int(变量) 将变量转化为整数类型
float(变量) 将变量转化为浮点类型
str(变量) 将变量转化为小数类型
"""

str1 = '9'
num1 = int(str1)
print(num1, type(num1), sep=',')

str2 = '9.'
num2 = float(str2)
print(num2, type(num2), sep=',')
