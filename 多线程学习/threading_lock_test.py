#! /usr/bin/python3
# -*- coding:utf-8 -*-


import threading
import time

count = 0


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock.acquire()      # acquire获得，先加锁
        temp = count + 1
        time.sleep(0.001)
        count = temp
        lock.release()      # 当count修改完成后再释放锁


lock = threading.Lock()     # lock对象，就是threading.Lock的一个实例
threads = []
for _ in range(1000):
    thread = MyThread()
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(f'Final count: {count}')
