"""
    sub函数 替换内容
"""

import re

text = "Hello, my email is example@example.com and my phone number is 123-456-7890."

res = re.sub(r'\d', 'X', text)  # Replace all digits with 'X'

print(res)
