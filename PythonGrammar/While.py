"""
while True:
    print("123")
"""


a = 1
sums = 0
while a <= 1031313:
    sums = sums + a
    a = a + 1

print(sums)

"""
break & continue
"""

while True:
    s = input("输入一段话:")
    if s == 'q':
        break   # 停止当前循环
    if "马化腾" in s:
        print("输入的话有关键字")
        continue    # 停止本次循环开始下次循环
    print("输入的一段话:"+s)

# 1-100内所有的奇数

a = 1
while a <= 100:
    if a % 2 == 1:
        print(a)
    a = a + 1

