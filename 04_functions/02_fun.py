"""
    解包传参：将列表、元组、字典解包成多个参数传给函数
"""

def func(a, b, c):
    print(a, b, c)

func(1,2,3)
func(a=1,b=2,c=3)

list1=[2,1,3]
func(*list1)

tuple1=(2,1,3)
func(*tuple1)

dict1={'a':1,'b':2,'c':3}
func(**dict1)
