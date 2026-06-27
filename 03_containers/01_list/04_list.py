list1 = [1, 2, 3, 4, 5]

print(list1)

del list1[1]

print(list1)

list2 = [[1, 2, 3], ['a', 'b', 'c'], [False, True]]

for item in list2:
    # print(item)
    for value in item:
        print(value)

print('----------列表推导式-----------')

list1 = [i for i in range(5)]
print(list1)

list1 = [i for i in range(5) if i % 2 == 0]

print(list1)

print('---------------------') 