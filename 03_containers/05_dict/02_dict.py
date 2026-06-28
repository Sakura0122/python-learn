dict1 = {'name': 'zhangsan', 'age': 18}

keys = dict1.keys()
print(keys)
values = dict1.values()
print(values)
items = dict1.items()
print(items)

for key in keys:
    print(key)

for value in values:
    print(value)

for (key, value) in items:
    print(key, value)

del dict1['name']
print(dict1)