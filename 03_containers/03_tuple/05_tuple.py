"""
    元组不可变性
    元组不可变 表示元组在内存中的地址不能改变
    至于元组中元素是否可以改变 要根据元素的类型来决定
"""

tuple1 = (1, 2, 3, 4, 5)

print(tuple1[0])
# tuple1[0] = 3

print(id(tuple1))
tuple1 = tuple1 + (6, 7, 8)
print(tuple1)
print(id(tuple1))

tuple2 = (1, 2, 3, [4, 5, 6])
print(tuple2)
print(tuple2[3])
tuple2[3].append(7)
print(tuple2)
