#! /usr/bin/python3
# -*- coding:utf-8 -*-


from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid} LoopCount: {count}')


if __name__ == '__main__':
    processes = []
    for i in range(3, 5):
        p = MyProcess(i)
        processes.append(p)
        p.daemon = True
        p.start()
    for p in processes:
        p.join(1)   # 给join方法传递一个超时参数，代表最长等待秒数，子进程在指定秒数之内完成，超时会被强制返回，主进程不会再等待

print('Main Process ended')
