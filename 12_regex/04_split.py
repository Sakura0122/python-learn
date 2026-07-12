"""
    sub函数 替换内容
"""

import re

text = "苹果，橘子；香蕉|西瓜"

res = re.split(r'[，；|]', text)

print(res)
