"""
递归
自己调自己
"""
import os
filePath = "D:/Python/Workspace/"
# print(os.listdir(filePath))


def func(filePath, n):
    lst = os.listdir(filePath)
    for i in lst:
        if os.path.isdir(os.path.join(filePath, i)):
            print("\t" * n + i)
            func(os.path.join(filePath, i), n+1)
        else:
            print("\t"*n + i)


func(filePath, 0)
