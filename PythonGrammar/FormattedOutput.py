"""
格式化输出
%s: 字符串的占位符，可以放置任何内容（数字）
%d: 数字的占位符
"""

a = 108
s = "这个数是%d" % a
print(s)    # 这个数是108

a = "108"
s = "这个数是%s" % a
print(s)    # 这个数是108

a = 108
s = "这个数是%s" % a
print(s)    # 这个数是108

a = 108
s = "这个数是%s"
print(s)    # 这个数是%s

name = 'alex'
# print("%s已经喜欢了沙河%2的女生" % name)    TypeError: not enough arguments for format string
print("%s已经喜欢了沙河%%2的女生" % name)     # alex已经喜欢了沙河%2的女生
print("skrwu已经喜欢了沙河%2的女生")      # skrwu已经喜欢了沙河%2的女生


num1 = 10
num2 = 20
num3 = num1 + num2
print("我用%d这个数去加%d这个数，最后得到%d这个数" % (num1, num2, num3))
# 我用10这个数去加20这个数，最后得到30这个数


