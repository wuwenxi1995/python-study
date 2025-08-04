# -*- coding: utf-8 -*-
# @Time    : 2025/8/4 16:56
# @Author  : wuwenxi

import threading as t
import time
import random
from collections import deque

"""
餐厅
"""


class Restaurant(t.Thread):
    def __init__(self, waiter_num: int = 5, chef_num: int = 3):
        super().__init__(name="restaurant")
        self.waiter_num = waiter_num
        self.chef_num = chef_num
        # 服务员
        self.waiter = [Waiter(self) for _ in range(waiter_num)]
        # 厨师
        self.chef = [Chef(self) for _ in range(chef_num)]
        # 订单
        self.order = BlockingQueue()
        self.order_num = 0

    def start(self):
        for c in self.chef:
            c.start()
        super().start()

    def run(self):
        while True:
            if self.order_num > 200:
                print("打烊了")
                break
            time.sleep(random.random() * 5)
            self.waiter[random.randrange(0, self.waiter_num)]()
            self.order_num += 1


"""
    服务员
"""


class Waiter:
    def __init__(self, r: Restaurant):
        self.r = r
        # 顾客
        self.customers: {Order: None, Customer: None} = {}

    def __call__(self, *args, **kwargs):
        c = Customer()
        # 下单
        o = c.order(self)
        self.r.order.put(o)
        self.customers[o] = c

    def consume(self, order):
        # 制作完成 上菜
        c = self.customers.get(order)
        c.consume(order)
        del self.customers[order]


"""
    订单
"""


class Order:

    def __init__(self, waiter: Waiter):
        self.waiter = waiter


"""
    厨师
"""


class Chef(t.Thread):
    def __init__(self, restaurant: Restaurant):
        super().__init__()
        self.restaurant = restaurant

    def run(self):
        while True:
            order = self.restaurant.order.get()
            if order is None:
                continue
            print(f"厨师{t.current_thread().name}拿到订单, 开始做菜")
            time.sleep(random.random() * 5)
            print(f"厨师{t.current_thread().name}拿到订单, 做菜完毕")
            order.waiter.consume(order)


"""
    顾客
"""


class Customer:

    @staticmethod
    def order(waiter: Waiter):
        return Order(waiter)


class BlockingQueue:
    def __init__(self):
        self._lock = t.RLock()
        self._queue = deque()
        self._condition = t.Condition()

    def put(self, item):
        with self._lock:
            self._queue.append(item)
        if self._queue.__len__() == 1:
            self._condition.notify_all()

    def get(self):
        while True:
            if self._queue.__len__() < 1:
                self._condition.wait()
                continue
            with self._lock:
                item = self._queue.popleft()
                if item is not None:
                    return item

    def __len__(self):
        return len(self._queue)


if __name__ == '__main__':
    restaurant = Restaurant()
    restaurant.start()
