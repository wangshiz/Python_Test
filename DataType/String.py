"""
字符串处理
"""
text = "Runoobs"
print(text)  # 输出字符串 Runoobs
print(text[0:-1])  # 输出第一个索引到倒数第二个索引（不包含所以是倒数第二个索引）的所有字符 Runoob
print(text[-6:-1])  # 输出倒数第六个索引到倒数第二个索引的所有字符 unoob
print(text[-1:-6])  # 输出空字符串，输出倒数第一个索引到倒数第5个索引的所有字符，这里step默认是正数，只能从左往右取，所以是空字符串
print(text[-1:-6:-1])  # 输出倒数第一个索引到倒数第5个索引（左开右闭），sboon
print(text[-6:-1:-1])  # 这种也是输出空字符串，因为只能从右往左取
print(text[0])  # 输出字符串第一个字符 R
print(text[-1])  # 输出倒数第一个字符 s
print(text[2:5])  # 输出从第三个索引开始到第五个索引字符 noo
print(text[2:])  # 输出从第三个开始的后的所有字符 noobs
print(text * 2)  # 输出字符串两次 RunoobsRunoobs
print(text + "Test")  # 链接字符串 RunoobsTest
print("-------------")
'''
Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
'''
print('Ru\noob')  # Ru
# oob
print(r'Ru\noob')  # Ru\noob

print('ru\toob')  # ru   oob

word1 = "aaa" \
        "bbb" \
        "ccc"
print(word1)  # aaabbbccc
word2 = """ddd
eee
fff"""
print(word2)  # dddeeefff
word3 = '''ggg
hhh
iii'''
print(word3)  # ggghhhiii
print("-------------")
"""
注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
"""
word = "Python"
print(word[0], word[5])  # P n  第0个索引和第5个索引
print(word[-1], word[-3])  # n h (倒序 -1是最后一个索引，以此类推，-3是倒数第三个索引)
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
# %%
s = "12345678"
print(s[1:5:3])  # 从索引1开始，到索引5结束（不包含），每3位取一个数 25
print(s[1::3])  # 从索引1到最后，每3位取一个数 258
print(s[6:2:-2])  # 从索引6开始，到索引2结束（不包含），每2位取一个数 75 (- 表示反着来)
print(s[6:2:2])  # 这个取不到值，因为最后一位写反了
print(s[7::-2])  # 从索引7开始，每2位取一个数 8642 (取反)
print(s[-1:-6:-2])  # 从索引-1开始（最后一位），到索引-6（倒数第6位），反取，每2位取一个数 864
print(s[-1:-6:2])  # 这个取不到值，因为最后一位是从左往右取
print(s[-6:-1:2])  # 从索引-6（倒数第6位），到索引-1（最后一位）正取，每2位取一个数 357
# %%
"""
Attention
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""

s = " tiny bit of reason. "
# 字符串大写
print(s.upper())
# 字符串小写
print(s.lower())
# 字符串首字母大写  tiny bit of reason. ，因为这里首字母是一个空格
print(s.capitalize())
# 大小写转换
print(s.swapcase())
# 被空格隔开的首字母大写
print(s.title())
# 字符串居中，并且两边用*填充至29
print(s.center(29, "*"))  # **** tiny bit of reason. ****
print('hi'.center(3, "-"))  # -hi

# 去两边的空格
print(s.strip())
# 去掉两边的内容 这个只会从最开头识别
print(s.strip("tiny"))  # tiny bit of reason. (因为这里开始不是tiny所以直接返回原始字符串)
print('tinytinyatinytiny'.strip('tiny'))  # a(因为这里两头连续识别到了各2个tiny，所以这里返回a)
# 去掉左边的空格
print(s.lstrip())
# 去掉左边的内容
print(s.lstrip('tiny'))
# 去掉右边的空格
print(s.rstrip())
# 去掉右边的内容
print(s.rstrip('tiny'))
# 替换2个字符串
print('tinytinyatinytiny'.replace("tiny", "小明", 2))
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
# 判断字符串是否只包含十进制字符串，定义一个十进制字符串，只需要在字符串最前面定义一个u(python3不需要)
print('123'.isdecimal())  # true
print(u'abc'.isdecimal())  # false

# 计算字符长度
print(len(snum))
print(snum.__len__())

# 遍历
for i in snum:
    print(i)

# 原样输出
s = "abc" + "\nss%sp" % "dd"
print(s)  # abc
# ssddp 这里会优先执行%s % dd（替换）
print(repr(s))  # 'abc\nssddp'

# 判断字符是否在ascii码里
s = ascii("a")
print(s)  # 'a'
s = ascii("中")
print(s)  # '\u4e2d'

# 这是一个类型错误，意味着Python无法识别你使用的信息。在这个示例中，Python发现你使
# 用了一个值为整数（int）的变量，但它不知道该如何解读这个值（见）。Python知道，这个变
# 量表示的可能是数值23，也可能是字符2和3。像上面这样在字符串中使用整数时，需要显式地指
# 出你希望Python将这个整数用作字符串。为此，可调用函数str()，它让Python将非字符串值表示
# 为字符串
# message = "Happy " + age + "rd Birthday!"
age = 23
message = "Happy " + str(age) + "rd Birthday!"


