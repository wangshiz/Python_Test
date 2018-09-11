"""
身份运算符
身份运算符用于比较两个对象的存储单元
运算符	描述	实例
is	    is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
"""
a = 20
b = 20
c = 10

print(a is b)       # True
print(id(a) == id(b))   # True
print(a is not b)   # False
print(id(a) != id(b))   # False

"""
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个。 
== 用于判断引用变量的值是否相等。
"""



