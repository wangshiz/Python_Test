s = "abc"
s1 = s.join("非常可乐")     # 把字符串s插入到"非常可乐"中
print(s1)   # 非abc常abc可abc乐

s = "_".join(["alex", "wuse", "taibai"])    # 把列表变成字符串
print(s)    # alex_wuse_taibai

s = "_".join({"key1": "value1", "key2": "value2"})
print(s)    # key1_key2

