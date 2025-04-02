"""
1. 函数
    1.1. 使用def关键字进行函数定义,函数名与括号内的形参列表
    1.2. 参数引用：引用变量时，首先，在局部符号表里查找变量，然后，是外层函数局部符号表，
        再是全局符号表，最后是内置名称符号表
    1.3. 在调用函数时会将实际参数（实参）引入到被调用函数的局部符号表中；因此，实参是使用 '按值调用'来传递的
    1.4. 函数中不返回return时，默认返回None。函数执行完毕退出也返回 None
2. 函数定义
    2.1 默认值参数, 定义函数是参数值可以默认赋值, 在调用函数时, 如果不传该参数则使用默认值;
        如果默认参数为可变对象如列表、字典，多次调用可能修改参数内容
        def ask_ok(prompt, retries=4, reminder='Please try again!'):
            while True:
                reply = input(prompt)
                if reply in {'y', 'ye', 'yes'}:
                    return True
                if reply in {'n', 'no', 'nop', 'nope'}:
                    return False
                retries = retries - 1
                if retries < 0:
                    raise ValueError('invalid user response')
                print(reminder)

            # 以下调用均正确
            ask_ok('Do you really want to quit?')
            ask_ok('Do you really want to quit?', 2)
            ask_ok('Do you really want to quit?', 2, '')
    2.2 关键字参数
        2.2.1 kwarg=value 形式的 关键字参数 也可以用于调用函数, 用参数名指定传入哪个参数
            def function(a, b=1, c=2, d=4):
              print(a, b, c, d)
            该函数由一个必选参数a，三个可选参数b、c、d组成, 以下函数调用均正确
            function(1,c=3,d=1) ==> 输出: 1,1,3,1
            function(1,b=10) ==> 输出: 1,10,2,4
        2.2.2 函数调用时，关键字参数必须跟在位置参数后面;所有传递的关键字参数都必须匹配一个函数接受的参数;关键字参数的顺序并不重要;
            不能对同一个参数多次赋值; 以下函数调用错误
            function(c=3,1) ==> 关键字参数后面存在位置参数，错误
            function(1,a=3) ==> 同一个参数多次赋值
            function(e=4) ==> 未知参数
        2.2.3 当函数参数为元组、字典时, 调用函数时的参数需要与函数关键字参数顺序一致
            def cheeseshop(kind, *arguments, **keywords):
                print("-- Do you have any", kind, "?")
                print("-- I'm sorry, we're all out of", kind)
                for arg in arguments:
                    print(arg)
                print("-" * 40)
                for kw in keywords:
                    print(kw, ":", keywords[kw])
            可以使用以下方式调用函数：
            cheeseshop("Limburger", "It's very runny, sir.",
                       "It's really very, VERY runny, sir.",
                       shopkeeper="Michael Palin",
                       client="John Cleese",
                       sketch="Cheese Shop Sketch")

    2.3 特殊参数, 为了控制参数传递方式, 可以使用/和*来分割参数, / 前为仅位置参数, /和*间既可以为位置参数也可以为关键字参数,
        *后为仅关键字参数
        2.3.1 函数定义:
            def function(only_pos, /, pos_and_kwd, *, only_key):
                pass
            其中：only_pos传参必须为位置参数, pos_and_kwd可以为位置参数或关键字参数,only_key 必须为关键字参数
            注意：如果函数中未定义/或*, 则可以用位置参数或关键字参数
            函数示例：
                def f1(arg):
                    print(arg)
                def f2(arg,/):
                    print(arg)
                def f3(/,arg): ==> 函数定义异常
                def f4(*,arg):
                    print(arg)
                def f5(arg1,/,arg2,*,arg3):
                    print(arg1,arg2,arg3)

                f1(1) ==> 输出：1
                f1(arg=1) ==> 输出: 1
                f2(2) ==> 输出：2
                f2(arg=2) ==> 异常调用, 函数申明/, arg为仅位置参数
                f4(3) ==>  异常调用, 函数申明*, arg为仅关键字参数
                f4(arg=3) ==> 输出:3
                f5函数以下调用均正确, 其他调用都错误
                f5(1,1,arg3=1) ==> 1,1,1
                f5(1,arg2=1,arg3=1) ==> 1,1,1
        2.3.2 参数有歧义，可以为位置参数也可以为关键字参数, 可能与字典产生冲突
            def f(name, **keymap):
                return 'name' in keymap
            f(1,**{'name':23})
            在这个函数中'name'与第一个关键字参数绑定, 因此函数不可能返回True

            如果将第一个参数限定为仅位置参数, 函数将返回True
            def f1(name, /, **keymap):
                return 'name' in keymap
            f1(1, **{'name',23}) ==> 输出:True
        2.3.3 特殊参数总结
            1. 使用仅限位置形参，可以让用户无法使用形参名。形参名没有实际意义时，强制调用函数的实参顺序时，
                或同时接收位置形参和关键字时，这种方式很有用。
            2. 当形参名有实际意义，且显式名称可以让函数定义更易理解时，阻止用户依赖传递实参的位置时，才使用关键字
            3. 对于 API，使用仅限位置形参，可以防止未来修改形参名时造成破坏性的 API 变动
    2.4 任意实参列表, 在可变数量的实参之前，可能有若干个普通参数; 实参包含在元组内；可变参数后的参数只能为仅限关键字参数;
        与java中不同的是, java中可变实参后不能再跟其他参数
        def f(arg1,arg2,*args):
            pass
        以下调用均正确
        f(1,2,'one','two','three')
        f(arg1=1,arg2=2,'one','two')

        def f1(*args,sep='/')
            return sep.join(args)
        仅限以下调用方式
        f1('one','two','three') ==> 输出: 'one/two/three'
        f1('one','two','three',sep=',') ==> 输出: 'one,two,three'

    2.5 解包实参列表
        2.5.1 函数调用要求独立的位置参数, 如果实参在元组或列表中, 可以使用*将实参从元组或列表解包出来
            arg = [3, 6]
            b = list(range(*arg)) ==> [3,4,5]

        2.5.2 如果参数列表在字典中, 可以用**将实参解包出来, 字典中key只能包含参数且必须包含必填参数
            def f(a,b='com',c='cn'):
             print(a,b,c)

            b = {'a':'wwx','b':'axl','c':'wrn'}
            f(**b) ==> 输出:'wwx','axl','wrn'
            b1 = {'b':'axl','c':'wrn', 'd':'xxx'}
            f(**b1) ==> 调用异常, 字典中包含实参列表中不存在的参数d, 字典中没有参数a

    2.6 lambda 表达式
        2.6.1 创建匿名函数, 该函数只能是单个表达式; 与嵌套函数定义一致, lambda表达式可以引用包含作用域中的变量
        def inc(n):
            return lambda x:x+n
        f = inc(10) ==> 新函数
            可以理解为 def f(x):
                        return 10+x
        print(f(0)) ==> 输出：10
        print(f(2)) ==> 输出：12

        2.6.2 把匿名函数用作传递的实参
        pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
            key类似java中集合排序传入的Comparator比较器,
            lambda pair: pair[1]为比较的键
        pairs.sort(key=lambda pair: pair[1])
        print(pairs)
"""

'''
lambda表达式
'''

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


def inc(n):
    return lambda x: x + n


f = inc(10)
print(f(0))
print(f(2))

'''
 解包参数
'''


def f(a, b='com', c='cn'):
    print(a, b, c)


b = {'a': 'wwx', 'b': 'axl', 'c': 'wrn'}
f(**b)

a = list(range(3, 9))
print(a)

a1 = [3, 6]
b = list(range(*a1))
print(b)

'''
特殊参数
'''


def f1(name, /, **keymap):
    return 'name' in keymap


f1(1, **{'name': 23})


def f5(arg1, /, arg2, *, arg3):
    print(arg1, arg2, arg3)


f5(1, 1, arg3=1)
f5(1, arg2=1, arg3=1)

'''
关键字参数
'''


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def function(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


def function1(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


function(1000)
print()
r = function1(100)
print('function1:', r)
print()
