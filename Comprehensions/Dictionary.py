"""
字典推导式
"""

dic = {"a": "b", "c": "d"}

new_dic = {dic[key]: key for key in dic}
print(new_dic)

lst1 = ["alex", "wusir", "taibai", "ritiao"]
lst2 = ["red", "blue", "green", "yellow"]

new_dic2 = {lst1[i]: lst2[i] for i in range(len(lst1))}
print(new_dic2)