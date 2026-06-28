dict1 = {'name': 'zhangsan', 'age': 18}

dict2 = {'a':'A','b':'B'}

dict1.update(dict2)
print(dict1) 

print(dict1.setdefault('name','lisi'))