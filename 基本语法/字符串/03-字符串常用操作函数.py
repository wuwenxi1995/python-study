"""
常用操作函数
    find('substr' ,start=, end=): 查找字符串中找到第一个子串substr的起始索引位置; start,end限制查询字符串中起始和结束范围内是否包含子串
    index('substr', start=, end=): 与find函数一样, 不同的是找不到子串回抛出异常
    count('substr', start=, end= ): 统计子串substr出现次数
    replace('old_str', 'new_str', count=): count参数指定替换old_str几次
    split('str', count=): count参数指定切分字符串多少次
    capitalize(): 将字符串第一个字符大写
    lower(): 将字符串中大写字符转为小写
    islower(): 判断字符串是否全部为小写组成
    upper(): 将字符串中小写转为大写
    isupper(): 判断字符串是否全部为大写组成
    startswith('str',strat,end): 字符串是否以字符串str开头
    endswith('str',strat,end): 字符串是否以字符串str结尾
    isspace(): 判断是否为空格字符串
    title(): 将字符串每个单词首字母大写
    istitle(): 判断字符串中每个单词首字母是否大写
    isdecimal(): 判断字符串中的字符是否都是十进制数字字符,仅识别最严格的十进制数字字符（如 '0' 到 '9'），不包括其他特殊形式的数字
    isdigit(): 与 isdecimal() 相比，除了包括所有十进制数字（即 isdecimal() 判定为真的字符），还包括其他数字字符，例如上标和下标数字、罗马数字、以及来自其他语言的数字表示法
    lstrip(): 删除字符串左边字符
    rstrip(): 删除字符串右边字符
    strip(): 删除字符串中所有空白字符
"""

h = 'hello world'

_replace_str = h.replace('l', 'L', 2)
print('str replace: ', _replace_str)

_split_str = h.split(' ', 2)
print('str split: ', _split_str)

cp = h.capitalize()
print('capitalize: ', cp)

sw = h.startswith('s', 1, 9)
ew = h.endswith('s', 1, 9)

print(f'str startswith \'s\' : {sw}, endswith \'s\' : {ew}')

isspace = ' '.isspace()

title = h.title()
print(f'title: {title}, istitle: {title.istitle()}')

h.lstrip()
h.rstrip()
h.strip()

num = '23'
print(f'isdigit: {num.isdigit()}, isdecimal: {num.isdecimal()}')

