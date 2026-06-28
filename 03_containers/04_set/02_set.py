set1 = {1, 2, 3}
set1.update({4})
set1.update([5, 6, 7])
print(set1)

set2 = set1.union({8, 9})
print(set2)

set1.discard(1)
# set1.remove(1) 删除不存在的回报错

set1.clear()
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.difference(set2)
print(set3)

set1.difference_update(set2)
print(set1)

print('---------------')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set3 = set1.intersection(set2)
print(set3)

print(set1 | set2)

print(set1 & set2)

print(set1 - set2)

print(set1 ^ set2)

