"""
编码和解码
encode()    编码  返回类型：byte
decode()    解码
"""

s = "alex"
bs = s.encode("utf-8")  # 把字符串编码成utf-8的形式
print(bs)

s = "饿了么"
bs = s.encode("GBK")    # 把字符串编码成GBK的形式
print(bs)   # b'\xb6\xf6\xc1\xcb\xc3\xb4'

s = "中"
print(s.encode("utf-8"))
print(s.encode("GBK"))

# decode()解码
bs = b'\xb6\xf6\xc1\xcb\xc3\xb4'
s = bs.decode("GBK")
print(s)    # 饿了么

# GBK → utf-8
bs = b'\xb6\xf6\xc1\xcb\xc3\xb4'
s = bs.decode("GBK")
bss = s.encode("utf-8")
print(bss)      # b'\xe9\xa5\xbf\xe4\xba\x86\xe4\xb9\x88'
