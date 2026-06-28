tuple1 = (1, 2, 3, 4, 5)

print(tuple1)
print(type(tuple1))

gen_tuple2 = (x for x in range(10))
print(gen_tuple2)
tuple2 = tuple(gen_tuple2)
print(tuple2)

print(tuple2[0])
print(tuple2[0:5])
print(tuple2[-1])
