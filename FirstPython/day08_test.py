"""
文件a.txt内容：每一行内容分别为商品名字，加钱，个数
"""
list = []
sum = 0
f = open("text/a", mode="r", encoding="utf-8")
for i in f:
    lis1 = i.split(" ")
    dic = {'name': lis1[0], 'price': int(lis1[1]), 'amount': int(lis1[2])}
    sum += int(lis1[1])*int(lis1[2])
    list.append(dic)

print(list)
print(sum)
f.close()

list2 = []
f = open("text/a1", mode="r", encoding="utf-8")
s = f.readline().split()
# ss = f.read()
# print(ss)
for k, v in enumerate(f):
    ss = v.split()
    dic = {}
    for i, j in enumerate(ss):
        dic[s[i]] = j
    list2.append(dic)
print(list2)
f.close()

