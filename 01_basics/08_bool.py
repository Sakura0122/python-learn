"""
    c语言里没有bool类型 使用int代替 0为false 非0为true
    python延续了这种规则 True可以理解为1 False可以理解为0
    True和False被设计为全局单例对象
    None 0 0.0 '' [] () {} False 在python中都等价于false 其他值都等价于true
"""

a = True
b = False
print(a)
print(b)
print(type(a))
print(type(b))
print(a == 1)
print(b == 0)
