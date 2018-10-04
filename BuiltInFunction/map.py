"""
映射函数
语法：map(function, iterable)可以对可迭代对象中的每一个元素进行映射，
分别取执行function
返回一个map可迭代对象
"""

# 计算列表中每个元素的平方
lst = [2, 4, 6, 8, 10]
mp = map(lambda s: s**2, lst)
print(mp)
print("__iter__" in dir(mp))
print("__next__" in dir(mp))
print(list(mp))


'''
map还可以处理多个函数, 对下角标
'''
lst1 = [1, 2, 4, 5, 8]
lst2 = [20, 30, 40, 50, 60]
mp2 = map(lambda x, y: x+y, lst1, lst2)
print(list(mp2))
