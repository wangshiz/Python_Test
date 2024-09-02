class Student:
    school = '北京大学'

    name = None,
    sex = None
    age = None
    __id_card = None  # 私有成员变量

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'{self.name}, {self.age}, {self.sex}'

    def __lt__(self, other):
        return other.age < self.age

    def __le__(self, other):
        return other.age <= self.age

    def __gt__(self, other):
        return other.age > self.age

    def __ge__(self, other):
        return other.age >= self.age

    def __eq__(self, other):
        return other.age == self.age

    @classmethod
    def onlyName(cls, name):
        return cls(name, None, None)

    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex

    def getName(self):
        return self.name

    # 私有成员方法
    def __getIdCard(self):
        return self.__id_card

    def setIdCard(self, id_card):
        self.__id_card = id_card

    def getIdCard(self):
        return self.__getIdCard()
