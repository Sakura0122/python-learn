a = 1
b = 2


def add(a, b):
    return a + b

if __name__ == "__main__":
    """
        在本模块中 __name__ 都是 __main__
        在其他模块中 __name__ 是模块名
    """
    print(__name__)
    print("我被调用了")