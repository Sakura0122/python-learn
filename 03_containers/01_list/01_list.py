list1 = [1, 2, 3, 4, 5]

print(list1)
print(type(list1))

print(list1[0])
print(list1[1])
# print(list1[10])
print(list1[:])
print(list1[1:3])
print(list1[::2])
print(list1[::-1]) 
print(list1[-1])

print('-' * 20)

list1.append(6)
print(list1)
list1.insert(0, 0)
print(list1)
list1.pop()
print(list1)
list1.remove(3)
print(list1)
list1.clear()
print(list1)
