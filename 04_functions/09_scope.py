list1 = [1, 2, 3]


def fun1():
    list1[1] = 666


fun1()
print(list1)

num = 100


def fun2():
    global num
    num = 200


fun2()
print(num)


def fun3():
    a = 100

    def fun4():
        nonlocal a
        a = 200
        print(a)

    fun4()
    print(a)


fun3()
