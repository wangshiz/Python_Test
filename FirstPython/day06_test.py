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
