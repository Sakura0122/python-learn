"""
    可变长参数：*args
"""

def func(a, *nums):
    print(a, nums)


func(1, 2, 3, 4)

def func(a, *nums,b):
    print(a, nums, b)

func(1, 2, 3, 4, b=5)

