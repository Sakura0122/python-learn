"""
    python中所有数据全部属于对象 都属于引用传递
    在函数体内对参数的修改是否会影响原变量 完全取决于是可变类型还是不可变类型
"""
import copy


def fun1(a):
    a = a + 1
    print('a:', a)


def fun2(a):
    a[0] = a[0] + 1
    print('a:', a)


b = 1
fun1(1)
print('b:', b)

c = [1, 2, 3]
fun2(c)
print('c:', c)

d = copy.deepcopy(c)
fun2(c)

print('c:', c)
print('d:', d)
