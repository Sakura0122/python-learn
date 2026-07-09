"""
    进程间使用Queue通信
    Queue特点 先进先出
"""
import random
import time
from multiprocessing import Manager
from multiprocessing.pool import Pool


def put_data(queue):
    for i in range(10):
        num = random.randint(1, 10)
        print(f"向队列中存放数据：{num}")
        queue.put(num)
        time.sleep(0.3)


def get_data(queue):
    for i in range(10):
        print('*' * queue.get())


if __name__ == '__main__':
    queue = Manager().Queue()

    pool = Pool(2)
    pool.apply_async(func=put_data, args=(queue,))
    pool.apply_async(func=get_data, args=(queue,))
    pool.close()
    pool.join()

    print("主进程执行完毕")