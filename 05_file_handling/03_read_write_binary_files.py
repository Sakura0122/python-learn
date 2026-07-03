"""
    读写二进制文件
    读取 rb read binary
    写入 wb write binary
"""

reader = open("C:\\Users\\Admin\\Pictures\\2.jpg", 'rb')
read_data = reader.read()
reader.close()

writer = open("./resources/1.jpg", 'wb')
writer.write(read_data)
writer.close()
