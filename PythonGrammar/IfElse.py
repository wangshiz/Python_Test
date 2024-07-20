gender = input("你是男的还是女的？")
if gender == '男':
    print("不放你进来")
elif gender == '女':
    age = input("你多大了啊？")
    if int(age) <= 40:
        print("放你进来")
    else:
        print("不放")
else:
    print("打死都不放进来")

a = 50
b = 10
if int(input("input")) == a:
    print(a)
elif int(input("input")) == a:
    print(a)
elif int(input("input")) == a:
    print(a)
else:
    print("error")
