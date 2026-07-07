"""
    当前案例展示类装饰器的使用
    计数器
"""


class Logger:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        print("日记开始")
        res = self.func(*args, **kwargs)
        self.count += 1  # 每次调用函数计数加一，用于统计函数被调用的次数
        print(f"函数{self.func.__name__}被调用了{self.count}次")
        print("日记结束")
        return res


@Logger
def add():
    print("执行数据库添加操作")
    return 100


add()
add()
add()
