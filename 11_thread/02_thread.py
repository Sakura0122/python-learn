import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        for i in range(10):
            print(f"线程名称：{self.name}打印数据{i}")
            time.sleep(0.1)


if __name__ == "__main__":
    t1 = MyThread("线程A")
    t2 = MyThread("线程B")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
