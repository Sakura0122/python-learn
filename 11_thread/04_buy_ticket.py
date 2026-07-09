import threading as td
import time

tickets = 10

lock = td.Lock()


def buy_ticket():
    global tickets
    while True:
        time.sleep(1)

        # 上锁
        lock.acquire()
        if tickets == 0:
            break
        tickets -= 1
        print(f"{td.current_thread().name}抢到了第{10 - tickets}张票，还剩{tickets}张票")
        # 解锁
        lock.release()
    print("票卖完了")


if __name__ == "__main__":
    t1 = td.Thread(target=buy_ticket, name="张三")
    t2 = td.Thread(target=buy_ticket, name="李四")
    t3 = td.Thread(target=buy_ticket, name="王五")
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
