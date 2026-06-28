str1 = 'Hello World'
print(str1)
print(str1[0])
print(str1[0:5])
print(str1[-1])

print('ld' in str1)

str1 = str1.replace('l', '*')
print(str1)

print('-------------------')

str1 = 'abc abc abc'
list1 = str1.split(' ')
print(list1)
print(','.join(list1))

print('-------------------')

str1 = ' abc  '
print(str1.strip())

print(str1.removeprefix(' '))

str1 = 'abc'
print(str1.upper())
print(str1.lower())

str1 = 'student_name'
print(str1.title())
print(max(str1))

str1 = 'abc def'
print(str1.find('def'))
print(str1.find('xyz'))

print(str1.index('def'))

print(str1.count('a'))

