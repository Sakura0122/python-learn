"""
    os.walk()函数 遍历目录
"""
import os

for root, dir_name, file_name in os.walk('./resources'):
    print('当前目录', root)
    print('目录列表', dir_name)
    print('文件列表', file_name)
