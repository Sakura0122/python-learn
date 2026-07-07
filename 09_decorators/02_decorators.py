def conn_decorator(func):
    def wrapper(*args, **kwargs):
        print("打开数据库连接")
        res = func(*args, **kwargs)
        print("关闭数据库连接")
        return res

    return wrapper


@conn_decorator
def add(a, b,c):
    print("执行数据库添加操作", a, b, c)
    return 100


print(add(100, 200, c=3))
