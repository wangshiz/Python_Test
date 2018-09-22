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
