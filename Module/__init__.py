# 只有这个文件存在就算python包

# 导入不同模块的同名功能
# from CustomModule2 import test的test方法顶掉了from CustomModule import test
from CustomModule import test
from CustomModule2 import test

test(1, 2)

# 通过__all__变量，控制import*
__all__ = ['CustomModule', 'CustomModule2']