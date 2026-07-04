"""
    with关键字是语法糖，用于简化try except finally的写法
"""

try:
    reader = open("a.txt", "r", encoding="utf-8")
    print(reader.read())
except OSError as e:
    print(e)
finally:
    reader.close()

with open("a.txt", 'r') as r:
    print(r.read())
