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
list = [1, 2, 3]
list2 = [1, 2, 3]

print(id(a))    # 得到内存地址 8791439038080
print("id(list)", id(list))     # 30630472
print("id(list2)", id(list2))     # 30630472

# 小数据池，会对字符串进行缓存，为了节省内存
print("id(a)", id(a))   # 8791439038080
print("id(b)", id(b))   # 8791439038080

# 小数据池（常量池）：把我们使用过的值 存储在小数据池中，供其他的变量值使用。
# 小数据池给数字和字符串使用，其他数据类型不存在


a = "aaaaaaadadadsa@#!$@#@#!$aaaaaaaaa" * 1000
b = "aaaaaaadadadsa@#!$@#@#!$aaaaaaaaa" * 1000
print(id(a), id(b))

a = True
b = True
print(id(a), id(b))

print(a is b)       # True
print(id(a) == id(b))   # True
print(a is not b)   # False
print(id(a) != id(b))   # False


# 区别
list = [1, 'y', 3]
a = 'y'
print(id(list[1]))
print(id(a))

"""
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个。
   判断的是内存地址
== 用于判断引用变量的值是否相等。
   判断的是左右两端的值        
"""



