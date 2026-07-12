"""
    findall函数 找到字符串中所有匹配内容
    以列表形式返回所有匹配内容
"""

import re

text = "Hello, my email is example@example.com and my phone number is 123-456-7890."

result = re.findall(r'\d', text)

if result:
    print("Match found:", result)
else:
    print("No match found")
