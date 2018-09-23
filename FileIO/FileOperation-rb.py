f = open("singer", mode="rb")   # 读取的内容直接就是字节
bs = f.read()
f.close()
print(bs.decode("utf-8"))
