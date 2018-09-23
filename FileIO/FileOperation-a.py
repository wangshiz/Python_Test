"""
追加内容
"""
f = open("./text/mode", mode="a", encoding="utf-8")
f.write(", spring")
f.flush()
f.close()