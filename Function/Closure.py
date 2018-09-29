"""
闭包
在内层函数中调用了外层函数的变量，叫闭包
闭包可以让一个局部变量可以常驻内存
"""


def fun1():
    name = "alex"   # 常驻内存

    def fun2():
        print(name)
    return fun2


ret = fun1()
ret()   # 执行的是fun2()


from urllib.request import urlopen


def fun():
    content = str(urlopen("http://webtest.qinqinhealth.com/shopxx/").read(), "utf-8")

    def inner():
        return content
    return inner


fn = fun()
content = fn()
print(content)