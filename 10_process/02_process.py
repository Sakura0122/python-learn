"""
    多进程方式3：进程池的方式
"""

import os
import time
from multiprocessing import Pool


def task(task_name):
    print(f"进程池执行任务{task_name}开始执行，进程池id:{os.getpid()}")
    time.sleep(0.2)
    print(f"任务{task_name}执行完毕")

if __name__ == '__main__':
    pool = Pool(3)
    for i in range(10):
        pool.apply(task, args=(i,))
        # pool.apply_async(task, args=(i,))
    pool.close()
    pool.join()
    print("主进程执行完毕")
