"""
只写文件
"""
f = open("text/mode", mode="w", encoding="utf-8")    # w 写会把之前的清空
f.write("kate")
f.flush()   # 刷新
f.close()
