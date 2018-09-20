# 4
string = 'k:1|k1:2|k2:3|k3:4'
strArr = string.split("|")
dic = {}
for item in strArr:
    sets = item.index(":")
    dic.setdefault(item[0:sets], int(item[sets+1:len(item)]))
else:
    print(dic)

# key
strArr = string.split("|")
dic = {}
for item in strArr:
    k, v = item.split(":")
    dic[k] = int(v)
else:
    print(dic)


# 5
li = {11, 22, 33, 44, 55, 66, 77, 88}
dic = {"k1": [], "k2": []}
for el in li:
    if el < 66:
        dic["k1"].append(el)
    else:
        dic["k2"].append(el)
else:
    print(dic)

# 6
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
for el in range(len(goods)):
    print(el+1, goods[el]["name"], goods[el]["price"])

while True:
    a = input("请输入您要查询的商品，按q退出")
    if a.upper() == 'Q':
        print("退出")
        break
    if not a.isdigit() or int(a) > len(goods):
        print("输入有误请继续输入")
        continue
    print(goods[int(a)-1]["name"], goods[int(a)-1]["price"])


# 7
menus = ("1.录入", "2.查询", "3.删除", "4.修改", "5.退出")
body_id = 1
bodies = {}
while True:
    for i in menus:
        print(i)
    a = input("请输入你要开始的功能：")
    if not a.isdigit() or int(a) > len(menus):
        print("您的输入有误，请再次输入：")
        break
    else:
        # 添加
        if int(a) == 1:
            print("进入录入环节：")
            while True:
                dicss = {}
                a1 = input("请输入姓名：")
                dicss["name"] = a1
                while True:
                    a2 = input("请输入体重：")
                    if not a2.isdigit() or not a2.isalpha():
                        dicss["weight"] = float(a2)
                        break
                    else:
                        print("您的输入有误，请重新输入")
                        continue
                while True:
                    a3 = input("请输入身高：")
                    if not a3.isdigit() or not a3.isalpha():
                        dicss["height"] = float(a2)
                        break
                    else:
                        print("您的输入有误，请重新输入")
                        continue
                dicss["BMI"] = dicss.get("weight") / dicss.get("height")**2
                bodies[body_id] = dicss
                body_id += 1
                print("恭喜您添加了一条记录", body_id, dicss)
                goon = input("您是否还要继续添加？y:是/其余值:否")
                if goon.islower() == 'y':
                    continue
                else:
                    break

        # 查询
        if int(a) == 2:
            print("进入查询环节：")
            for el in range(len(bodies)):
                print(bodies[el][0], bodies[el][1]["name"], bodies[el][1]["weight"], bodies[el][1]["height"], bodies[el][1]["BMI"])

        # 删除
        if int(a) == 3:
            print("进入删除环节")
            while True:
                a3 = input("请输入你要删除的序号")
                if a3.isdigit() or bodies.keys():
                    pass
                else:
                    continue







