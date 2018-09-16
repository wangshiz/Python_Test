a = "Runoobs"
print(a)        # 输出字符串 Runoobs
print(a[0:-1])  # 输出第一个到倒数第二个的所有字符 Runoob
print(a[-6:-1])  # 输出倒数第六个到倒数第二个的所有字符 unoob
print(a[-1:-6])  # 输出倒数第一个到倒数第二个的所有字符
print(a[0])     # 输出字符串第一个字符 R
print(a[-1])    # 输出倒数第一个字符 s
print(a[2:5])   # 输出从第三个开始到第五个字符 noo
print(a[2:])    # 输出从第三个开始的后的所有字符 noobs
print(a*2)      # 输出字符串两次 RunoobsRunoobs
print(a + "Test")     # 链接字符串 RunoobsTest

'''
Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
'''
print('Ru\noob')    # Ru
# oob
print(r'Ru\noob')   # Ru\noob

word1 = "aaa"\
    "bbb"\
    "ccc"
print(word1)     # aaabbbccc
word2 = """ddd
eee
fff"""
print(word2)    #dddeeefff
word3 = '''ggg
hhh
iii'''
print(word3)    #ggghhhiii

"""
注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
"""
word = "Python"
print(word[0], word[5])     # P n
print(word[-1], word[-3])   # n h
"""
与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
"""

# 我说："啥"
print("我说：\"啥!\"")  # 转义字符

print("我", end="")
print("是", end="")
print("啥", end="\n")

# 我是啥

print("我", "是", "啥")

# 我 是 啥

"""
步长
语法：s[初始位置:结束为止:步长]
"""

s = "12345678"
print(s[1:5:3])     # 从1-5，每3位取一个数 25
print(s[1::3])      # 从1到最后，每3位取一个数 258
print(s[6:2:-2])    # - 表示反着来，每2位取一个数 75
print(s[7::-2])     # 反取，每2位取一个数 8642
print(s[-1:-6:-2])  # 反取，每2位取一个数 864
print(s[-6:-1:2])   # 正取，每2位取一个数 357

"""
Attention
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""

s = "tiny bit of reason."
# 字符串大写
print(s.upper())
# 字符串小写
print(s.lower())
# 字符串首字母大写
print(s.capitalize())
# 大小写转换
print(s.swapcase())
# 被空格隔开的首字母大写
print(s.title())
# 字符串居中
print(s.center(29, "*"))
# 去两边的空格
print(s.strip())
# 去掉两边的内容
print(s.strip("tiny"))
# 去掉左边的内容
print(s.lstrip())
# 去掉右边的内容
print(s.rstrip())
# 替换2个字符串
print(s.replace("tiny", "小明", 2))
# 字符串切割
print(s.split(" "))

test = "alex alex want do alex"
test2 = test[5: 9].replace("alex", "sb")
print(test2)

# 判断字符串是否以xxx开始
print(s.startswith("tiny"))
# 判断字符串是否以xxx结尾
print(s.endswith("you"))
# 统计xxx在字符串第x位到第y位里出现的次数
print(s.count("of", 0, 20))
# 统计xxx在字符串第x位到第y位里出现的位置 没出现返回-1
print(s.find("of", 0, 20))
# 统计xxx在字符串第x位到第y位里出现的位置 没出现报错
print(s.index("of", 0, 20))
# 判断字符串是否由数字组成

'''
拓展，了解
'''
snum = "1233"
# snum = "" 这种情况一下函数只会返回false
# 判断字符串是否由数字组成，不包含小数点
print(snum.isdigit())
# 判断字符串是否由字母组成
print(snum.isalpha())
# 判断字符串是否由字母和数字组成
print(snum.isalnum())
# 判断字符串是否由数字组成(中英文)
print(snum.isnumeric())
# 判断字符串是否只包含十进制字符串，定义一个十进制字符串，只需要在字符串最前面定义一个u
print(snum.isdecimal())



# 计算字符长度
print(len(snum))
print(snum.__len__())


# 遍历
for i in snum:
    print(i)
