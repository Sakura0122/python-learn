for i in [1, 3, 5, 7, 9]:
    print(i)

print('-' * 20)

for i in range(1, 10, 2):
    print(i)

print('-' * 20)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end=' ')
    print()
