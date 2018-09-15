# 猜数字
import random

guessNum = random.randint(1, 100)
count = 0
a = 0
while True:
    a = input("请输入你要猜的数字")
    count = count + 1
    if int(a) > guessNum:
        print("您猜的数字大了请重新猜过")
    elif int(a) < guessNum:
        print("您猜的数字小了请重新猜过")
    else:
        print("猜对了你")
        print("这个数为%s，您共猜了%s" % (a, count))
        break
    continue
