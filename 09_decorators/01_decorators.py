def open_conn():
    print("打开数据库连接")


def close_conn():
    print("关闭数据库连接")
    print("*" * 20)


def conn_decorator(func):
    def wrapper():
        open_conn()
        res = func()
        close_conn()
        return res

    return wrapper


@conn_decorator
def add():
    print("执行数据库添加操作")
    return 100


@conn_decorator
def remove():
    print("执行数据库删除操作")


@conn_decorator
def update():
    print("执行数据库修改操作")


@conn_decorator
def get():
    print("执行数据库查询操作")


add()
remove()
update()
get()
print(add())