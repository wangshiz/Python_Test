a = "Runoobs"
print(a)        # 输出字符串 Runoobs
print(a[0:-1])  # 输出第一个到倒数第二个的所有字符 Runoob
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
Attention
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""
