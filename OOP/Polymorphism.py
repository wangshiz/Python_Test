class Animal:
    def speak(self, text):
        pass

class Dog(Animal):
    def speak(self, text):
        print("wangwang")

class Cat(Animal):
    def speak(self, text):
        print("miaomiao")


def speak(animal: Animal):
    animal.speak("123")


dog = Dog()
cat = Cat()
speak(dog)
speak(cat)
