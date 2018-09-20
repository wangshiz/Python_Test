"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。如果出现相同则后面那个key值会覆盖之前的key值。
"""
dicts = {}
pass
dicts['one'] = '1'
dicts[2] = '2'
dicts['one'] = '4'
print(dicts)    # {'one': '4', 2: '2'}

dit = dict()
dit[0] = 20
print(dit)      # {0: 20}

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(tinydict)             # {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(1, tinydict.keys())      # 拿到所有的key值 dict_keys(['name', 'code', 'site'])
print(type(tinydict.keys()))    # <class 'dict_keys'>
print(tinydict.values())    # 拿到所有的value值 dict_values(['runoob', 1, 'www.runoob.com'])
print(tinydict.items())     # 拿到所有的键值对

for item in tinydict.items():
    print(item[0])  # 获得key
    print(item[1])  # 获得value
    print(item)     # 获得元组

# 解构
a, b = 1, 2
print(a)
print(b)

# 所以上面的可以这样写

for k, v in tinydict.items():
    # k, v = item
    print(k, v)

'''
构造函数 dict() 可以直接从键值对序列中构建字典如下：
'''
dit1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dit1)     # {'Runoob': 1, 'Google': 2, 'Taobao': 3}
dit2 = {x: x**2 for x in (2, 4, 6)}
print(dit2)     # {2: 4, 4: 16, 6: 36}
dit3 = dict(Runoob=1, Google=2, Taobao=3)
print(dit3)     # {'Runoob': 1, 'Google': 2, 'Taobao': 3}


dit.setdefault(1, 21)
dit.setdefault(1, 22)   # 无效 因为这个字典里包含了key为1的值
print(dit.setdefault(1))    # 21

dit[0] = 23     # 赋值
print(dit)

dic = {"abc": "你去哪里了", "xiaoxue": "傻子哦", "尻": "ss", "wosan": "怒会"}
print(dic)
# 删除
# ret = dic.pop("xiaoxue")    # 返回key的value值
# del dic["abc"]
# 随机删
rets = dic.popitem()    # 返回元组
# print(ret)
print(rets)
print(dic)

# 对值进行操作
dic = {"id": 1, "name": "li", "money": 10000}
dic['money'] = dic['money'] - 500
print(dic)

dic1 = {1: 2, 2: 3, 3: 4}
dic2 = {"wo": "shi", 2: "diodio"}
dic1.update(dic2)   # 把dic2的内容更新到dic1中, 如果存在key 替换  不存在 添加
print(dic1)
print(dic2)


dic = {"及时雨": "宋江", "小李广": "花荣", "黑旋风": "李逵", "易大师": "剑圣"}
# dic["大宝剑"] = "盖伦"   # 新增
# dic["及时雨"] = "天老爷"  # 修改
print(dic["易大师"])   # 查询 如果没有这个key会报错
print(dic.get("易大师"))   # 查询 如果没有这个key不会报错返回None
print(dic.get("123", 233))    # 如果没有这个key，取233这个默认值

# 字典的嵌套
dic = {
    "name": "汪峰",
    "age": 58,
    "wife": {
        "name": "国际章",
        "salary": 18000,
        "age": 37
    },
    "children": [
        {"name": "老大", "age": 18},
        {"name": "老二", "age": 14}
    ]
}

print(dic["children"][1]["age"])
print(dic["wife"]["salary"])

"""
另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
"""
tinydict = {1: 'runoob', 2: 1, 3: 'www.runoob.com'}

print(tinydict.keys())
print("1" in tinydict.keys())