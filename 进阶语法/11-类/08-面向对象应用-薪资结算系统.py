# -*- coding: utf-8 -*-
# @Time    : 2025/7/29 22:41
# @Author  : wuwenxi

from abc import ABCMeta, abstractmethod

"""
某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。其中，部门经理的月薪是固定 15000 元；
程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。
"""


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """计算月薪"""
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000


class Programmer(Employee):

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05


emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')
