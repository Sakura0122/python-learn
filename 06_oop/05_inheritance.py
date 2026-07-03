# 动物
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# 狗
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return "Woof!"


# 猫
class Cat(Animal):
    def speak(self):
        return "Meow!"


d1 = Dog("Buddy", 3)
c1 = Cat("Whiskers")
print(d1.name, d1.age, d1.speak())
print(c1.speak())
