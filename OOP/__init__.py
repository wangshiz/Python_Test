# from Student import Student

import Student
import People
import SingleInheritance
stu = Student.Student(name='John', age=25, sex=1)
print(stu.getAge())
print(stu.school)

print('============')

stu2 = Student.Student.onlyName(name='tom')
print(stu2.getName())
print(stu2.getSex())
print(stu2.school)
stu2.setIdCard('10010101010101')
print(stu2.getIdCard())
peo = People.People(name='sam', age=10, sex=1)
peo.whatToDo(stu)

print('============')
primary_stu = SingleInheritance.PrimarySchoolStudents('Jimmy', 1, 10, 16)
print(primary_stu)
