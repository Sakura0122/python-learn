"""
    通过线程池创建线程
"""

from concurrent.futures import ThreadPoolExecutor
import threading as td
import time

def task():
    print(f"线程名称：{td.current_thread().name}开始执行任务")
    time.sleep(1)
    print(f"线程名称：{td.current_thread().name}执行任务完毕")


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as pool:
        for i in range(10):
            pool.submit(task)

