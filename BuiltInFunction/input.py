"""
input 输出
作用：从外部获取钱变量的值
"""

# 等待输入（阻塞）
age = input("请输出您的年龄：")
print("age", age)

# 请输出您的年龄：17
# 17

'''
程序从input()方法里获取到的值是字符串类型
'''
age2 = input("请输入你的年龄")
if int(age2) < 18:
    print("不能饮酒")
else:
    print("可以")

'''
输入一串数，模拟加法计算
'''
sum = 0
num = input("请输入一串数")
numlist = num.split("+")
for i in numlist:
    sum += int(i)
print(sum)
