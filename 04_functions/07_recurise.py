"""
    递归函数：在函数体内调用函数本身
"""


def fib(n: int):
    if n <= 2: return 1;
    return fib(n - 1) + fib(n - 2)


print(fib(10))


def get_sum(n: int):
    if n <= 1: return 1
    return n + get_sum(n - 1)

print(get_sum(100))