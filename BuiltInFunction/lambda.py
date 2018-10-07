"""
lambda 匿名函数
x 为参数
: 后面是函数体(直接return的内容)
语法：lambda 参数:返回值
"""

a = lambda x: x*x
print(a)        # <function <lambda> at 0x0000000001D3D268>
print(a(6))     # 36
'''
查看方法名
'''
print(a.__name__)   # <lambda>

b = lambda x, y: x*y
print(b(3, 6))  # 18


