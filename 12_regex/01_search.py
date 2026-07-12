"""
    search函数 查找内容匹配 从任何位置满足要求都可以
    如果满足则返回match对象，否则返回None
"""

import re

text = "Hello, my email is example@example.com and my phone number is 123-456-7890."

result = re.search(r'\d', text)

if result:
    print("Match found:", result.group())
else:
    print("No match found")
