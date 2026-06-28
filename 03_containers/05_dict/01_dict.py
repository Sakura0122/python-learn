dict1 = {}
print(dict1)
dict1 = {'name': 'zhangsan', 'age': 18}
print(dict1)


print(dict1['name'])
# print(dict1['address']) 取不到报错
print(dict1.get('address'))
print(dict1.get('address','深圳'))

dict1['name'] = 'zhaosi'
print(dict1)