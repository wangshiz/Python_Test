"""
动态传参
"""

'''
位置参数：a，b
动态参数：*xx
默认参数：c=..
关键字参数：**xx

'''


# 位置参数 > 动态参数 > 默认参数
def eat(a, b, *food, c=5):
    print("我要吃", food)  # 动态接收的是元组数据
    print(a, b, food, c)
    print(globals())    # 查看全局作用域中所有名字
    print(locals())     # 查看当前作用域中所有名字


eat(1, 2, 3, 4, 5, c=6)


# 动态接收关键字参数
# *位置参数
# **关键字参数
def func(**food):
    print(food)     # 返回一个字典


func(a=1, b=2, c=3, d=4)


# 位置，动态，默认值，关键字
def fun2(a, b, *foods, c=3, **cars):
    print(a, b, foods, c, cars)


fun2(1, 2, 3, 4, 5, 6, c=3, d=4, e=5)


def fun3(a, b):
    print(a, b)


# */** 运用在实参上，解包元组/字典形式结构
fun3(*(1, 2))

fun3(**{"a": 2, "b": 2})


def fun4(*food):
    print(food)


a = (1, 2, 3, 4, 5)


fun4(*a)


