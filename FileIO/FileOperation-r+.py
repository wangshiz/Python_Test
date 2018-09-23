"""
r+模式，默认情况下光标在文件的开头，必须先读，后写
"""

# f = open("getname", mode="r+", encoding="utf-8")
#
# s = f.read()
# f.write("纳什")
# f.flush()
# f.close()
# print(s)

# f = open("flash", mode="r+", encoding="utf-8")
# s = f.read(3)
# ss = f.read(3)
# print(s)
# print(ss)
# f.write(",好好")
# # 如果之前没有进行任何操作，write的时候默认在开头写
# # 如果之前进行了其他操作，write在最后写
# f.close()


f = open("txt/flash", mode="r+", encoding="utf-8")
s = f.read(3)   #读取三个字
f.seek(3)   # 移动到3字节这个位置
f.seek(0)   # 移动到开头
f.seek(0, 2)    # 移动到结尾
print(f.tell()) # 贯标位置
print(f.read())
f.close()



