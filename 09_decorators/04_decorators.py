"""
    带参数的装饰器 必须有三层函数嵌套
    最外层函数 负责接收参数
    第二层函数 负责返回实际的装饰器
    第三层函数 负责调用被装饰的函数
"""


def log_decorators(level):
    def acc_func(func):
        def log_inner(*args, **kwargs):
            print("日志开始,等级", level)
            res = func(*args, **kwargs)
            print("日志结束,等级", level)
            return res

        return log_inner

    return acc_func


@log_decorators(level=1)
def add(a, b, c):
    print("执行数据库添加操作", a, b, c)
    return 100

print(add(100, 200, c=3))