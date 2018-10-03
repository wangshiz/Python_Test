print("曹操", "刘备", "孙权", sep="_")

# 曹操_刘备_孙权

# hash
string = "name"
print(hash(string))

lst = [1, 2, 3, 4, 5]
lst2 = iter(lst)
print(lst2)
a = next(lst2)
print(a)


# 动态导入模块

name = input("请输入一个导入模块")
print(__import__(name))


print(help(str))

# callable 判断变量能否被调用
a = 10
print(callable(a))  # False


def func():
    pass


print(callable(func))   # True

# str转byte
a = bytes("中华", encoding="utf-8")
print(a)    # b'\xe4\xb8\xad\xe5\x8d\x8e'
a = a.decode("utf-8")
print(a)    # 中华

# str转byte数组
a = bytearray("abcd", encoding="utf-8")
print(a[0])     # a

# 查看byte在内存中的情况
s = memoryview(a)
print(s)    # <memory at 0x00000000026E04C8>

#
"""
format 
    字符串 居左居中居右
    数字 转义成x进制
    科学计数法
"""

# 可迭代长度
print(len("abc"))

# 枚举 索引从100开始
for i, j in enumerate("abc", 100):
    print(i, j)

'''
all()  可迭代对象中所有值为true  返回true
any()  可迭代对象中有一个值为true  返回true
'''
print(all([1, "aa", True]))  # True
print(all([0, None, True]))  # False
print(any([0, None, True]))  # True

'''
zip(a, b, c)  将多个可迭代对象通过下角标值变成一个个元组
所有元组组合到一起形成一个新的可迭代对象
如果长度不一致，则按最短长度的对象来作为新的对象的长度
'''

lst1 = ["aaa", "bbb", "ccc", "dddd"]
lst2 = ["111", "222", "333", "444", "555"]
lst3 = [0, 1, 2, 3]
print(zip(lst1, lst2, lst3))    # <zip object at 0x00000000028DF0C8>
for el in zip(lst1, lst2, lst3):
    print(el)

