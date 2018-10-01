"""
迭代器
可迭代对象：str，list，tuple，set，f，dict
"""
#                        可迭代的，迭代器
from collections.abc import Iterable, Iterator

# 所有的以上数据类型中都有一个函数__iter__()
# dir()来查看一个对象，数据类型中包含了哪些东西
list = [1, 2, 3]
print(dir(list))
s = "temmple"
print("__iter__" in dir(s))
print("__iter__" in dir(list))
print("__iter__" in dir(123))

lst = ["tom", "sam", "jerry", "teary"]
it = lst.__iter__()

print(it.__next__())    # tom
print(it.__next__())    # sam
print(it.__next__())    # jerry
print(it.__next__())    # teary


# 模拟for循环
it = lst.__iter__()
while True:
    try:
        name = it.__next__()
        print(name)
    except StopIteration:
        break

# 除了文件句柄，其他类型本身不是一个迭代器
list2 = [1, 2, 3]
print("__next__" in dir(list2))     # False
print(isinstance(list2, Iterable))  # True
print(isinstance(list2, Iterator))  # # False

it = list2.__iter__()
print(isinstance(it, Iterable))  # True
print(isinstance(it, Iterator))  # # True 迭代器里一定有__next__(),__iter__()


it = list2.__iter__()
print(it.__next__())    # 1
print(it.__next__())    # 2
print(it.__next__())    # 3


'''
迭代器特点：
    1.节省内存
    2.惰性机制
    3.不能反复，只能向下执行
'''

