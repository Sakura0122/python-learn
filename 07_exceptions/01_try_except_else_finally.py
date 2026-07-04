"""
    try except else finally 异常处理
    try:
        可能出错的代码
    except:
        出错时执行的代码
    else:
        没有出错时执行的代码
    finally:
        无论是否出错都会执行的代码
"""
try:
    print(a)
except:
    print("出错啦")

try:
    num1 = int(input("请输入被除数\n"))
    num2 = int(input("请输入除数\n"))
    print(num1 / num2)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("请输入正确的数字")
else:
    print("没有出错")
finally:
    print("无论是否出错，都会执行")
