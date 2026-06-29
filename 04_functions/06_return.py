"""
    有些函数在执行的时候 会返回一个结果给调用者 使用return语句
"""


def my_sum(a: int, b: int):
    return a + b


print(my_sum(1, 3))


def func():
    return 1, 2, 3, [4, 5, 6]


r1 = func()
print(r1)
r1, r2, r3, r4 = func()
print(r1, r2, r3, r4)
 