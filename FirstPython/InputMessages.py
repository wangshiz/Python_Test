# 字典录入  输入数字的时候要是float类型
# 可能会有bug

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
                    if not a2.isdigit() and not a2.isalpha():
                        dicss["weight"] = float(a2)
                        break
                    else:
                        print("您的输入有误，请重新输入")
                        continue
                while True:
                    a3 = input("请输入身高：")
                    if not a3.isdigit() and not a3.isalpha():
                        dicss["height"] = float(a3)
                        break
                    else:
                        print("您的输入有误，请重新输入")
                        continue
                dicss["BMI"] = dicss.get("weight") / dicss.get("height")**2
                bodies[body_id] = dicss
                print("恭喜您添加了一条记录", body_id, dicss)
                body_id += 1
                goon = input("您是否还要继续添加？y:是/其余值:否")
                if goon.lower() == 'y':
                    continue
                else:
                    break

        # 查询
        if int(a) == 2:
            print("进入查询环节：")
            for k, v in bodies.items():
                print(k, list(v.keys())[0], list(v.values())[0], list(v.keys())[1], list(v.values())[1],
                      list(v.keys())[2], list(v.values())[2], list(v.keys())[3], list(v.values())[3])

        # 删除
        if int(a) == 3:
            if len(bodies) == 0:
                print("该字典里没有值")
                continue
            print("进入删除环节")
            while True:
                a3 = input("请输入你要删除的序号")
                if a3.isdigit() and int(a3) in bodies.keys():
                    deleteValue = bodies.pop(int(a3))
                    a = input("序号{}:{}已删除，是否需要继续删除：（是：y/否：其他任意值）".format(int(a3), deleteValue))
                    if a.lower() == 'y':
                        continue
                    else:
                        break
                else:
                    print("您的输入有误，请继续输入！")
                    continue
            continue

        # 修改
        if int(a) == 4:
            print("进入修改环节")
            if len(bodies) == 0:
                print("该字典里没有值")
                continue
            while True:
                a4 = input("请输入你要修改的序号")
                if a4.isdigit() and int(a4) in bodies.keys():
                    print("该用户的信息为：", bodies[int(a4)])
                    print("进入录入环节：")
                    dicss = {}
                    a1 = input("请输入姓名：")
                    dicss["name"] = a1
                    while True:
                        a2 = input("请输入体重：")
                        if not a2.isdigit() and not a2.isalpha():
                            dicss["weight"] = float(a2)
                            break
                        else:
                            print("您的输入有误，请重新输入")
                            continue
                    while True:
                        a3 = input("请输入身高：")
                        if not a3.isdigit() and not a3.isalpha():
                            dicss["height"] = float(a2)
                            break
                        else:
                            print("您的输入有误，请重新输入")
                            continue
                    dicss["BMI"] = dicss.get("weight") / dicss.get("height") ** 2
                    bodies[int(a4)] = dicss
                    a = input("序号{}已修改，修改的值为{}是否需要继续修改：（是：y/否：其他任意值）".format(int(a4), bodies[int(a4)]))
                    if a.lower() == 'y':
                        continue
                    else:
                        break
                else:
                    print("您的输入有误，请继续输入！")
                    continue
            continue

        # 退出
        if int(a) == 5:
            print("退出")
            break
