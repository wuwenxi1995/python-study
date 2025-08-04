# -*- coding: utf-8 -*-
# @Time    : 2025/8/4 10:35
# @Author  : wuwenxi

import time
import concurrent.futures as f
import threading as t
import random


def run():
    print("running, 当前线程名: ", t.current_thread().name, end="\n")
    time.sleep(random.random())
    print(f"当前线程名:{t.current_thread().name}, done...", end="\n")


'''
    手动创建线程
'''

thread = t.Thread(target=run(), name="custom thread")
# 启动线程
thread.start()
# 等待线程完成
thread.join()


class MyThread(t.Thread):

    def __init__(self):
        super().__init__(name="MyThread")

    def run(self):
        print("MyThread running")
        time.sleep(0.5)
        print("done")


mythread = MyThread()
mythread.start()
mythread.join()

''' 
    通过线程池创建
'''
with f.ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    for _ in range(5):
        f = executor.submit(run)
        futures.append(f)
    # 等待任务完成
    for f in futures:
        f.result()
