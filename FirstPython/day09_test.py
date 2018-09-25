"""
数据录入，并添加到文件
"""

def chicken_data(name, age, edu, sex="男"):
    f = open("text/student", mode='a', encoding='utf-8')
    f.write(name+"_"+str(age)+"_"+sex+"_"+edu+"\n")
    f.flush()
    f.close()


while 1:
    name = input("请输入名字")
    age = input("请输入年龄")
    sex = input("请输入性别")
    edu = input("请输入学历")
    if sex == '':
        chicken_data(name, age, edu)
    else:
        chicken_data(name, age, edu, sex)
    a = input("是否退出")
    if a.lower() == 'q':
        break

