"""
追加内容
"""
f = open("./txt/mode", mode="a", encoding="utf-8")
f.write(", spring")
f.flush()
f.close()