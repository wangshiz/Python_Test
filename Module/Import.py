"""
Python模块（Module）是一个Python文件，以.py结尾  模块能定义函数，类和变量。模块里也能包含可执行的代码

模块导入语法：
[from 模块名] import  [模块 | 类 | 变量 | 函数 | *] [as 别名]

常用组合形式：
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
"""
import time
# 直接使用import导入一个包下所有功能
# import time
# print('开始')
# time.sleep(1)
# print('结束')

# 使用from导入time的sleep功能
# from time import sleep
# sleep(1)

# 跟import类似 但是写法跟import类似
from time import *

import Module.CustomModule

sleep(1)

# 给模块和方法设置别名
import time as t
t.sleep(2)
from time import sleep as s1
print('开始')
sleep(1)
print('结束')
s1(2)
print('结束2')

from Module import *
Module.CustomModule.test(1, 2)
Module.CustomModule2.test(1, 2)

from numpy import *
