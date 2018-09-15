"""
逻辑运算符
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
运算符	逻辑表达式	描述
and	    x and y	    布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	    x or y	    布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	    not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
"""
a = 10
b = 20

'''
python里0为false，其他数为true
'''

print(a and b)      # 20
print(a or b)       # 10
a = 0
print(a and b)      # 0
print(a or b)       # 20
print(not(a and b))     # True
print(not(a or b))      # False

'''
优先级：
在 not or and 同时存在的情况下 先算括号内容 再算 not 再算 and 最后再算 or
'''
print(not (3 > 1) and True or False and False or (3 > 1 and True))
# True


'''
and: 如果为true 返回 y 值
or: 如果为true 返回 x 值
'''
print(0 and 1)      # 0
print(1 and 0)      # 0
print(1 and 2)      # 2
print(1 or 0)       # 1
print(0 or 1)       # 1
print(0 or 0)       # 0
print(1 or 3)       # 3

print(2 < 1 and 4 > 6 or 3 and 4 > 5 or 6)      # 6

