"""
生成器
"""


def fun():
    print("aa")
    yield "bb"
    print("cc")
    yield "dd"


ac = fun()
print(ac.__next__())
print(ac.__next__())


'''
send
效果和__next__()差不多，并且给上一个yield赋值
'''


def func():
    print("AA")
    a = yield "11"
    print(a)
    print("BB")
    b = yield "22"
    print(b)
    print("CC")
    c = yield "33"
    print(c)
    yield "OVER"


g = func()
g.__next__()    # 开头需要
g.send("aa")    # 将aa赋值给a
g.send("bb")    # 将bb赋值给b
g.send("cc")    # 将cc赋值给c


'''
生成器赋值给列表
'''


def func2():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


lst = list(func2())    # 必须是可迭代对象
print(lst)


'''
生成器表达式
用小括号包起来
好处：列表推导式比较耗内存，一次性加载，生成器表达式几乎不占内存
'''


def func3():
    print(111)
    yield 222


g = func3()
g1 = (i for i in g)
g2 = (i for i in g1)

print(list(g))
print(list(g1))
print(list(g2))


lst = (i for i in range(10))
print(lst.__next__())
print(lst.__next__())


def add(a, b):
    return a + b


def test():
    for r_i in range(4):
        yield r_i


g = test()

# 惰性机制的体现
for n in [2, 10]:
    g = (add(n, i) for i in g)
    # g = (add(n, i) for i in add(n, i) for i in test())
print(list(g))




