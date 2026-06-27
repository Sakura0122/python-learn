list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']

print(list1 + list2)

print(list1 * 3)

print(list2 * 3)

print('------------------------------')

list1[1:3] = [666]
print(list1)

print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))

print('------------------------------')

for i in list1:
    print(i)

for i, v in enumerate(list1):
    print(i, v)

print('------------指定start---------------')
for i, v in enumerate(list1, start=1):
    print(i, v)
