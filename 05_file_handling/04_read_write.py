"""
    读写文件的优化操作
    我们之前的read都是无参的，将文件一次性读取到内存中
    这样做在文件较大的时候会占用大量内存
    我们可以使用read(size)方法来指定每次读取的文件大小，从而避免占用大量内存
"""
with open('./resources/1.jpg', 'rb') as src, \
        open('./resources/2.jpg', 'wb') as dst:
    while True:
        data = src.read(1024)
        if not data:
            break
        dst.write(data)
