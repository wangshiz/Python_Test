import Student
import People
# 多继承
# 一个类继承多个类，按照顺序从左向右依次继承
# 多继承中，如果父类有同名方法或属性，先继承的优先级高于后继承
class JuniorHighSchoolStudents(Student.Student, People.People):
    # __school_time = None
    #
    # def __init__(self, name, sex, age, school_time):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    #     self.__school_time = school_time
    #
    # def __str__(self):
    #     return f'{self.name}, {self.age}, {self.sex}, {self.__school_time}'
    pass
