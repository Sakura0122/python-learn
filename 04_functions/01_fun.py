"""
    函数即一系列代码指令的集合 用于解决特定的问题 可以反复调用
    必须先定义后调用
    函数定义的格式：
        def 函数名(参数列表):
            函数体
            return 返回值
"""


def print_sign():
    for _ in range(10):
        print('-', end='')
    print()

print_sign()
print_sign()

# 控制符号数量
def print_sign(num):
    for _ in range(num):
        print('-', end='')
    print()
print_sign(20)

# 控制符号数量和类型
def print_sign(num, char):
    for _ in range(num):
        print(char, end='')
    print()
print_sign(20, '*')
print_sign(char='&',num=30)