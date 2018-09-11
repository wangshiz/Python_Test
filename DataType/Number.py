# Number（数字）

"""
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
像大多数语言一样，数值类型的赋值和计算都是很直观的。
内置的 type() 函数可以用来查询变量所指的对象类型。
"""

a, b, c, d = 1, 1.0, True, 4+3j
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

'''
此外还可以用 isinstance 来判断：
'''

a = 1
print("a的值为"+str(a))
print("a是否为int类型："+str(isinstance(a, int)))
print("a是否为float类型："+str(isinstance(a, float)))
# 1
# a是否为int类型：True
# a是否为float类型：False


'''
isinstance 和 type 的区别!important
'''


class FatherA:
    pass
# pass 啥都不做


# 继承写法：B继承
class ChildB(FatherA):
    pass


result1 = isinstance(FatherA(), FatherA)
result2 = type(FatherA()) == FatherA
print(result1, result2)   # True True

result3 = isinstance(ChildB(), FatherA)
result4 = type(ChildB()) == FatherA
print(result3, result4)   # True False


'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''

'''
当你指定一个值时，Number 对象就会被创建：
'''
var1 = 1
var2 = 2

print(var1)  # 1
print(var2)  # 2

'''
使用del语句删除一些对象引用。
'''
del var1
# print(var1)  # NameError: name 'var1' is not defined
print(var2)  # 2


# del var1[,var2[,var3[....,varN]]]


'''
数值运算
'''
print(5+4)      # 加法 result = 9
print(4.3-2)    # 减法 result = 2.3
print(3*7)      # 乘法 result = 21
print(2/4)      # 除法，得到一个浮点数 result = 0.5
print(2//4)     # 除法，得到一个整数 result = 0
print(17%3)     # 取余 result = 2
print(2**5)     # 乘方 result = 32

'''
这里//得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
'''
print(7//2)     # 3
print(7.0//2)   # 3.0

'''
不同类型的数混合运算时会将整数转换为浮点数：
'''
print(3*3.75/1.5)   # 7.5
print(7.0/2)        # 3.5

















