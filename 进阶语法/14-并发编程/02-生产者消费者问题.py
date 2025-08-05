# -*- coding: utf-8 -*-
# @Time    : 2025/8/4 16:56
# @Author  : wuwenxi

import threading as t
import time
import random
import uuid
import logging
import os
from datetime import datetime
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor, Future

"""
餐厅
"""

log_file = os.path.join(os.getcwd(), f'log{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')

# 配置日志格式
log_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"
)

# 创建根记录器
log = logging.getLogger("restaurant")
log.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(log_format)

# 添加处理器到记录器
if not log.handlers:
    log.addHandler(file_handler)
    log.addHandler(console_handler)

executor = ThreadPoolExecutor(max_workers=10)


class Restaurant:
    def __init__(self, waiter_num: int = 5, chef_num: int = 3):
        self.waiter_num = 1 if waiter_num < 1 else waiter_num
        self.chef_num = 1 if chef_num < 1 else chef_num
        # 服务员
        self.waiter = [Waiter(self, index) for index in range(self.waiter_num)]
        # 厨师
        self.chef = [Chef(self)]
        # 订单
        self.order = Queue(maxsize=200)
        self.order_num = 0

    def start(self):
        for w in self.waiter:
            w.start()
        for c in self.chef:
            c.start()
        self.run()

    def run(self):
        log.info("餐厅开始营业...")
        while True:
            if self.order_num >= 10:
                log.info("打烊了...")
                if not self.order.empty():
                    self._stop()
                return
            time.sleep(random.randrange(1, 3))
            self.waiter[random.randrange(0, self.waiter_num)]()
            self.order_num += 1
            log.info(f'待处理订单{self.order.qsize()}, 总订单数为: {self.order_num}, 厨师数: {len(self.chef)}')
            if (self.order.qsize() > 20 and len(self.chef) < 2) or (self.order.qsize() > 30 and len(self.chef) < 3):
                new_chef = Chef(self)
                self.chef.append(new_chef)
                new_chef.start()
            elif self.order.qsize() > 50 and len(self.chef) < self.chef_num:
                for _ in range(len(self.chef), self.chef_num):
                    new_chef = Chef(self)
                    self.chef.append(new_chef)
                    new_chef.start()
            elif self.order.qsize() <= 5 and len(self.chef) > 1:
                chef = self.chef.pop()
                chef.undo()

    def _stop(self):
        if len(self.chef) < self.chef_num:
            new_chef = Chef(self)
            self.chef.append(new_chef)
            new_chef.start()
        for c in self.chef:
            c.join()
        for w in self.waiter:
            w.is_complete()
        executor.shutdown()


"""
    服务员
"""


class Waiter(t.Thread):
    def __init__(self, r: Restaurant, num: int):
        super().__init__()
        self.restaurant = r
        # 顾客
        self.customers: dict[Order, tuple[Customer, Future]] = {}
        self.orders = Queue(maxsize=200)
        self.num = 0
        self.w_name = '服务员' + str(num)
        self._condition = t.Condition(lock=t.Lock())
        self.stop = False

    def run(self):
        while not self.stop:
            with self._condition:
                while self.orders.empty() and not self.stop:
                    self._condition.wait()
            if self.stop:
                break
            try:
                order = self.orders.get(timeout=0.1)
                self.consume(order)
            except Empty:
                continue
        log.info(f"服务员{self.w_name}结束工作")

    def __call__(self, *args, **kwargs):
        c = Customer(self)
        # 下单
        o = c.choose()
        log.info(f"服务员{self.w_name}开始服务: {c}")
        self.restaurant.order.put(o)
        self.num += 1
        future = executor.submit(c.run)
        self.customers[o] = (c, future)

    def complete(self, order):
        log.info(f"服务员{self.w_name}从厨房拿到订单, 订单信息: {order.order_no}")
        self.orders.put(order)
        with self._condition:
            self._condition.notify()

    def consume(self, order):
        # 制作完成 上菜
        c = self.customers.get(order)
        c[0].consume()

    def order_complete(self, order):
        log.info(f'订单完成{order.order_no}')
        del self.customers[order]

    def is_complete(self):
        for o, (c, f) in self.customers.items():
            # 等待订单完成
            if not f.done():
                f.result()
                log.info(f'订单完成{o.order_no}')
        log.info(self)
        self.stop = True
        with self._condition:
            self._condition.notify()

    def __repr__(self):
        return f"服务员{self.w_name}完成工作, 共服务顾客{self.num}人"


"""
    订单
"""


class Order:
    food = ["汉堡", "薯条", "炸鸡", "牛排", "牛柳", "鸡翅", "意面", " pizza"]
    drink = ["可乐", "雪碧", "啤酒", "橙汁", "咖啡", "奶茶"]

    def __init__(self, waiter: Waiter):
        self.waiter = waiter
        self.order_no = uuid.uuid4()
        self.foods = []
        self.drunk = []

    def order(self, f=2, d=0):
        self.foods = random.sample(self.food, k=f)
        self.drunk = random.sample(self.drink, k=d)

    def __repr__(self):
        return f"订单号{self.order_no}, 选择主食{self.foods}, 选择饮料{self.drunk}"


"""
    厨师
"""


class Chef(t.Thread):
    def __init__(self, r: Restaurant):
        super().__init__()
        self.restaurant = r
        self.c_name = str(uuid.uuid4()).split("-")[0]
        self.working = True

    def run(self):
        while self.working:
            try:
                order = self.restaurant.order.get(timeout=10)
                if order is None:
                    self.restaurant.chef.remove(self)
                    break
                log.info(f"厨师{self.c_name}拿到订单, 订单信息: {order}, 开始做菜")
                time.sleep(random.randrange(2, 4))
                log.info(f"厨师{self.c_name}订单完毕")
                order.waiter.complete(order)
            except Empty:
                log.error(f"没有待处理订单, 厨师{self.c_name}停止工作")
                break

    def undo(self):
        self.working = False
        # 等待当前线程结束
        self.join()


"""
    顾客
"""


class Customer:

    def __init__(self, waiter: Waiter):
        self.order = None
        self.c_name = str(uuid.uuid4()).split("-")[0]
        self.queue = Queue(maxsize=1)
        self.waiter = waiter

    def run(self):
        # 阻塞队列, 等待制作完成
        self.queue.get()
        log.info(f"顾客{self.c_name}拿到菜")
        time.sleep(random.randrange(3, 5))
        log.info(f"顾客{self.c_name}用餐完毕")
        self.waiter.order_complete(self.order)

    def choose(self):
        self.order = Order(self.waiter)
        self.order.order(f=random.randrange(2, 5), d=random.randrange(1, 2))
        return self.order

    def consume(self):
        self.queue.put(self.order)

    def __repr__(self):
        return f"顾客{self.c_name}, 订单信息: {self.order}"


if __name__ == '__main__':
    restaurant = Restaurant()
    restaurant.start()
