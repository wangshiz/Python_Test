"""
Python数据类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
"""

a1 = '10'
b1 = int(a1, base=10)     # 将x转换为一个整数 base:进制
a2 = '101'
b2 = int(a2, 2)
a3 = '1234'
b3 = int(a3, 5)
a4 = '12334276'
b4 = int(a4, 8)
print(b1, b2, b3, b4)

a5 = 12
b5 = float(a5)      # 将x转换到一个浮点数
print(b5)   # 12.0

a6 = complex(1, 2)
print(a6)   # (1+2j)

a7 = "www"
b7 = str(a7)    # 将对象 x 转换为字符串  给用户看
print(b7)   # www
print(isinstance(b7, str))   # True

a8 = "www"
b8 = repr(a8)   # 将对象 x 转换为表达式字符串   给机器看
print(b8)   # 'www'
print(isinstance(b8, str))  # True


a9 = 7
b8 = eval('3 * a9')     # 用来简单计算在字符串中的有效Python表达式,并返回一个对象
print(b8)   # 21

a20 = "for i in range(10):print(i)"
b20 = exec(a20) # 0 1 2 3 4 5 6 7 8 9
print(b20)  # 用来相对复杂计算在字符串中的有效Python表达式,但不返回一个对象


a21 = """
def func():
    print("老王")
func()
"""
b21 = exec(a21)
print(b21)

a22 = "1+1"
b22 = compile(a22, "", mode="eval")
c22 = eval(b22)
print(c22)  # 2

a23 = "for i in range(3):print(i)"
b23 = compile(a23, "", mode="exec")
exec(b23)

# a24 = "asd=input('输入');print(asd)"
# b24 = compile(a24, "", mode="single")   # input用single
# exec(b24)
# print(b24)

a10 = 23
b10 = tuple(str(a10))   # 将序列 s 转换为一个元组
print(b10)       # (2, 3)


a11 = 'string'
b11 = list(a11)     # 将序列 s 转换为一个元组
print(b11)      # [s, t, r, i, n, g]

a12 = 'blueSkey'
b12 = set(a12)      # 将序列 s 转换为一个元组
print(b12)  # {'e', 'u', 'k', 'S', 'l', 'y', 'b'}

a13 = dict([('sss', 123), ('ttt', 456)])    # 创建一个字典。d 必须是一个序列 (key,value)元组。
print(a13)  # {'sss': 123, 'ttt': 456}

a14 = 'redsun'
b14 = frozenset(a14)    # 转换为不可变集合
print(b14)  # frozenset({'e', 's', 'u', 'r', 'n', 'd'})

a15 = 123
b15 = chr(a15)  # 将一个整数转换为一个字符
print(b15)  # {

a16 = 's'
b16 = ord(a16)  # 将一个字符转换为它的整数值
print(b16)  # 115

a17 = 15
b17 = hex(a17)  # 将一个整数转换为一个十六进制字符串
print(b17)  # 0xf

a18 = 16
b18 = oct(a18)  # 将一个整数转换为一个八进制字符串
print(b18)  # 0o20

a19 = 17
b19 = bin(a19)  # 将一个整数转换为一个二进制字符串
print(b19)  # 0b10001

# 绝对值
print(abs(-123))     # 123

# 五舍六入
print(round(1.49))   # 1

# 求商 余数
print(divmod(20, 3))    # 6, 2

# 求次幂
print(pow(10, 2))   # 10^2 = 100

# 求次幂的余数
print(pow(10, 2, 3))    # 10^2%3 = 1

# 求和
print(sum([1, 2]))  # 3

# min()最小值
# max()最大值


# ascii


# fun
for i in range(65536):
    print(chr(i), end=" ")
