"""
    写入文件时如果不存在会自动创建一个
    指定模式 w 或者 a
    w 覆盖写入
    a 追加写入
"""
file = open('./resources/2.txt', 'w')
file.write('hello world')
file.flush()  # 刷新缓冲区
file.close()
