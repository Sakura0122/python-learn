a = 10
print(a)
a += 5
print(a)  # 等同于 a = a + 5
a *= 2
print(a)  # 等同于 a = a * 2
a **= 2
print(a)  # 等同于 a = a ** 2
a //= 2
print(a)  # 等同于 a = a // 2
a %= 3
print(a)  # 等同于 a = a % 3

print('*' * 20)

# := 海象运算符
a = 0
print(a := 10 > 5)
print(a)
