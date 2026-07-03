class Person:
    home = "Earth"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("被回收了哦")

    def eat(self):
        print(self.name, "is eating")


p1 = Person("John", 36)
print(Person.home)
print(p1.name, p1.age)
p1.eat()

del p1