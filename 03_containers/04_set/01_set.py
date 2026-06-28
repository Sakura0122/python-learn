set1 = {1, 2, 3}
set2 = set([1, 2, 3])

print(set1)
print(set2)
set1.add(4)
set1.add(3)
print(set1)

set1.remove(3)
print(set1)

print(len(set1))
print(min(set1))
print(max(set1))
print(sum(set1))
