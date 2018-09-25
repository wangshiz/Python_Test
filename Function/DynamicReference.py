"""
动态传参
"""
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

func(a=1, b=2, c=3)