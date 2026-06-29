from functools import reduce
from typing import Callable


def operation(a: int, b: int, fun: Callable[[int, int], int]):
    return fun(a, b)


print(operation(1, 2, lambda a, b: a + b))
print(type(lambda a, b: a + b))

person_list = [
    {"name": "zhangsan", "age": 20},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 22}
]

print(sorted(person_list, key=lambda p: p['age']))

print([x for x in person_list if x['age'] > 20])

print(list(filter(lambda p: p["age"] > 20, person_list)))

print(reduce(lambda acc, p: acc + p['age'], person_list,0))
 