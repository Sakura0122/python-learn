"""
    数据类型和类型的判断
    type() 判断是否属于某个类型
    isinstance() 判断是否属于某个类型，或者属于某个类型的子类
"""

a = 10
print(type(a))
b = 2.5
print(type(b))
c = True
print(type(c))
d = False
print(type(d))
e = 'hello'
print(type(e))

print('a是否是int类型', isinstance(a, int))
print('b是否是float类型', isinstance(b, float))
print('c是否是int类型', isinstance(c, int))
print('c是否是bool类型', isinstance(c, bool))
print('d是否是bool类型', isinstance(d, bool))
print('e是否是str类型', isinstance(e, str))
