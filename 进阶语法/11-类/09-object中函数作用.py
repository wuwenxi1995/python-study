# -*- coding: utf-8 -*-
# @Time    : 2025/7/31 09:28
# @Author  : wuwenxi


class ObjectMethod(object):
    def __init__(self):
        super().__init__()

    def __new__(cls):
        return super().__new__(cls)

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __delattr__(self, __name):
        super().__delattr__(__name)

    def __eq__(self, __value):
        return super().__eq__(__value)

    def __hash__(self):
        return super().__hash__()

    def __ne__(self, __value):
        return super().__ne__(__value)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def __sizeof__(self):
        return super().__sizeof__()

    def __dir__(self):
        return super().__dir__()

    """
        魔方方法
    """

    '''
        函数式行为: 让对象可以像函数一样被调用或支持函数相关操作, 实现自己调用自己
        self() 实际调用的是__call__
        class Counter:
            def __init__(self):
                self.count = 0
            def __call__(self):
                self.count += 1
                return self.count
        
        counter = Counter()
        print(counter())  # 输出：1（第一次调用）
        print(counter())  # 输出：2（第二次调用）
    '''

    def __call__(self, *args, **kwargs):
        ...

    '''
        上下文管理, 
            __enter__ 进入 with 代码块时执行（返回资源）
            __exit__ 退出 with 代码块时执行（释放资源）
            
        class DatabaseConnection:
            def __enter__(self):
                print("连接数据库")
                return self  # 作为with语句的变量
            def __exit__(self, exc_type, exc_val, exc_tb):
                print("关闭数据库连接")  # 无论是否出错都会执行
        
        with DatabaseConnection() as db:
            print("执行查询...")  # 输出：连接数据库 → 执行查询... → 关闭数据库连接
    '''

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    '''
        与算术运算相关
    '''

    def __add__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    '''
        类型转换相关
    '''

    def __int__(self):
        pass

    def __float__(self):
        pass
