"""
    有精度损失 采用IEEE754标准
    对精度有要求可以采用Decimal模块 此类使用字符串方式
"""
from decimal import Decimal

a = 0.1
b = 0.2
c = a + b
print(c)


a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c)
