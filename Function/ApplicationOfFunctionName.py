"""
函数名的应用
函数名实际上就是一个变量
"""


def fun():
    print("这是fun()的内容")


# a = fun()

b = fun

# 函数名可以当作变量放到数据结构中
list = [fun, b]
print(list)
for el in list:
    el()


# 可以把方法名作为参数，传递给另外一个方法
def fun2():
    print("这是fun2()的内容")


def fun3(fun2):
    fun2()


fun3(fun2)


# 函数名可以当作返回值
def fun4():
    def fun5():
        print("这是fun5()的内容")
    return fun5


ret = fun4()
ret()



