"""
    多进程方式1：使用multiprocessing模块创建进程
"""

import multiprocessing as mp
import os
import time


# 编写函数 用于进程执行的任务
def task():
    for i in range(10):
        print(f"子进程{mp.current_process().name},进程id{os.getpid()}执行任务{i}")


if __name__ == '__main__':
    p1 = mp.Process(target=task)
    p2 = mp.Process(target=task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主进程执行完毕")
