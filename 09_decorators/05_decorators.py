"""
    类装饰器 本身就属于一个类
    类中可以定义变量 保存更多的数据
    类装饰器的优势：存变量 存配置 作缓存 作计数

    需要定义两个方法：__init__ __call__  __init__接收被装饰的函数 __call__执行被装饰的函数
"""


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("日记开始")
        res = self.func(*args, **kwargs)
        print("日记结束")
        return res

@Logger
def add(a, b, c):
    print("执行数据库添加操作", a, b, c)
    return 100

print(add(100, 200, c=3))