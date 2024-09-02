import Student
# 单继承
class PrimarySchoolStudents(Student.Student):
    __school_time = None

    def __init__(self, name, sex, age, school_time):
        super().__init__(name, age, sex)
        self.__school_time = school_time

    def __str__(self):
        return f'{self.name}, {self.age}, {self.sex}, {self.__school_time}'
