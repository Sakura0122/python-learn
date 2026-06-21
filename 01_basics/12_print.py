"""
    print函数 输出内容到控制台 默认换行
    不希望换行可以使用end参数指定其他字符，例如空格
    不希望用空格连接可以使用sep参数指定其他分隔符，例如逗号
    格式化输出 %s 字符串 %d 整数 %f 浮点数
    format函数 格式化输出 {} 占位符
"""
print("hello world")
print("hello", "world", sep="+")
print("hello", "world", end=" ")

print("*" * 10)

a = 10.2
b = 20
print("a=%d,b=%d" % (a, b))
print("a={0},b={1}".format(a, b))
