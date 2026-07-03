class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.__sex = sex


p1 = Person("赵四", -199, "你好")
print(p1.name)
print(p1._age)
print(p1._Person__sex)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


u1 = User('张三', 18)
print(u1.age)
u1.age = 19
print(u1.age)
