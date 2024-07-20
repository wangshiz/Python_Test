a = 1
b = 2
print(a + b)
print(a * b)
print(a // b)
print(a ** b)
print("woshishei")
print('woshishei')
print("""woshishei""")
print(a, b, "woshishei")
print(chr(91))
# 获取编码
print(ord("北"))
# 获取字符
print(chr(21271))

print(1, 2, 3, sep="", end="\n")

# print("123" + 3)  error TypeError: can only concatenate str (not "int") to str

# 百分号占位 %s转换成str类型
name = '我是谁'
message = 'check %s' % name
print(message)

name = '我是谁'
answer = "小王"
message = 'check %s, answer %s' % (name, answer)
print(message)

# 解决数字类型不能跟字符串相交
name = '我是谁'
answer = "小王"
no = 56
isPass = True
message = 'check %s, answer %s, 编号 %s, 是否通过 %s' % (name, answer, no, isPass)
print(message)

# %d 将内容转换为数字类型
# %f 将内容转换为浮点数类型
name = '我是谁'
answer = 11
no = 56.7
isPass = True
message = 'check %s, answer %d, 编号 %f, 是否通过 %s' % (name, answer, no, isPass)
print(message)



name = '我是谁'
answer = 11
no = 56.7
isPass = True
message = 'check %s, answer %5d, 编号 %.2f, 是否通过 %3s' % (name, answer, no, isPass)
print(message)
# 另外一种方式 这个方式不做任何处理，纯填充
print(f'check {name}, answer {answer}, 编号 {no}, 是否通过 {isPass}')
# 直接格式化表达式
message = 'check %s, answer %5d, 编号 %.2f, 是否通过 %3s' % (1 * 1, 2 + 1, 1.1 + 0.1, a == a)
print(message)
print(f'check {1 * 1}, answer {type(a)}, 编号 {1.2}, 是否通过 {a == b}')

if (a == 2):
    print(a == 2)
else:
    print(a == 2)