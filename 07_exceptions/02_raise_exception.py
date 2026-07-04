"""
    raise 用于抛出异常
    用于在合适的时机结束程序
"""


def get_sum(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("num1 和 num2 必须是数字")

    return num1 + num2

get_sum(1, "2")
