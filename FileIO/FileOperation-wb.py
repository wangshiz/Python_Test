f = open("mode", mode="wb")   # 读取的内容直接就是字节
f.write("你好呀".encode("utf-8"))
f.close()

# w, r, a === wb, rb,ab     b:处理非文本
