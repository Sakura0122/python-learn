"""
    进程间使用Queue通信 不使用线程池
    Queue特点 先进先出
"""
import random
import time
from multiprocessing import Queue, Process
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
    q1 = Queue()

    p1 = Process(target=put_data, args=(q1,))
    p2 = Process(target=get_data, args=(q1,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("主进程执行完毕")