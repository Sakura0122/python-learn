"""
    match case 语句：多分支选择结构，又称作模式匹配
    语法：
        match 变量:
            case 值1:
                语句1
            case 值2:
                语句2
            case _:
                语句3
"""

month = int(input("请输入月份："))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{month}月有31天")
    case 4 | 6 | 9 | 11:
        print(f"{month}月有30天")
    case 2:
        print(f"{month}月有28天")
    case _:
        print("输入的月份有误")
