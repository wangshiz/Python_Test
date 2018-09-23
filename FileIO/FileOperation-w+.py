f = open("writeread", mode="w+", encoding="utf-8")  # w+ 清空原来内容
f.write("今天天气好")
f.seek(0)
s = f.read()
print(s)
f.flush()
f.close()