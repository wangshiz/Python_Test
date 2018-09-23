import os

with open("./txt/eating", mode="r", encoding="utf-8") as f1,\
        open("./txt/eating_copy", mode="w", encoding="utf-8") as f2:
    # s = f1.read()
    # ss = s.replace("肉", "菜")
    # f2.write(ss)
    for line in f1:
        s = line.replace("菜", "肉")
        f2.write(s)
os.remove("./txt/eating")
os.rename("./txt/eating_copy", "./txt/eating")
