"""
成员运算符
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
运算符	描述
in	    如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
"""

a = 10
b = 5
lists = [1, 2, 3, 4, 5]
if 6 in lists:
    print("存在")
else:
    print("不存在")
if 4 in lists:
    print("存在")
else:
    print("不存在")

if a not in lists:
    print("不存在")
else:
    print("存在")
if b not in lists:
    print("存在")
else:
    print("不存在")

"""
不存在
存在
不存在
不存在
"""
