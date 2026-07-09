"""
    进程之间默认不共享全局变量 即每个进程独自访问一份全局变量
    多个进程访问多份 互不影响
"""
import os
from multiprocessing import Process


def func(build_list: list):
    for i in range(10):
        build_list.append(i)
        print(f"进程id:{os.getpid()}", build_list)


if __name__ == '__main__':
    list1 = []
    p1 = Process(target=func, name="进程A", args=(list1,))
    p2 = Process(target=func, name="进程B", args=(list1,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("主进程执行完毕")
