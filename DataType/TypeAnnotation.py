# 类型注解仅仅只是个备注 不会对程序有影响
# 基础数据类型注解
from typing import Tuple, List, Dict, Union

var_1: int = 1
var_2: float = 1.0
var_3: bool = True
var_4: str = "123"


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2]
my_tuple: tuple = (1, 2)
my_dict: dict = {"name": "tom"}

# 容器类型详细注解
my_list1: List[int] = [1, 2, 3]
my_tuple1: Tuple[int, str, bool] = (1, "123", True)
my_dict1: Dict[str, int] = {"name": 123}

# 在注释中进行类型注释
var_1 = 1  # type: int
var_2 = 1.0  # type: float
var_3 = True  # type: bool
var_4 = "123"  # type: str


def func():
    return 10


var_5 = func()  # type: int


# 对形参进行注解
def func1(x: int, y: int):
    return x + y


var_6 = func1(1, 2)


# 对返回值进行注解
def func2(x: list) -> list:
    return x


# union 类型
my_list: List[Union[int, str]] = [1, "1", 2, "2"]
my_dict: Dict[str, Union[int, str]] = {"tom": "1", "sam": 2}


def func3(x: List[Union[int, str]]) -> List[Union[int, str]]:
    return x
