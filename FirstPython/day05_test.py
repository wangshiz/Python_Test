# 1.字符串处理
li = ["TaiBai", "ale xC", "AbC", "egon", "ri TiAn", "WuSir", "aqc"]
li2 = []
for i in li:
    i = i.replace(" ", "")
    if i.capitalize().startswith("A") and i.endswith("c"):
        li2.append(i)
else:
    print(li2)

# 2.敏感字过滤
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
li2 = []
a = input("请输入文字：")
for i in li:
    if i in a:
        num = len(i)
        s = ""
        for c in range(num):
            s += "*"
        a = a.replace(i, s)
        li2.append(a)
    else:
        li2.append(a)
print(li2)

# 3 循环打印
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
for i in li:
    if isinstance(i, str):
        print(i.lower())
    elif isinstance(i, list):
        for c in i:
            if isinstance(c, str):
                print(c.lower())
            else:
                print(c)
    else:
        print(i)


# 4

