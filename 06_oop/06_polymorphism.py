"""
    多态：同一个事物 因为环境不同 产生不同的结果
    多态性：同一个方法调用，根据对象的类型，执行不同的方法
"""

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "汪汪汪！"

class Cat(Animal):
    def make_sound(self):
        return "喵喵喵~"

# 统一的调用接口
def animal_sound(animal_obj):
    print(animal_obj.make_sound())

# 创建对象
dog = Dog()
cat = Cat()

# 传递不同的对象，调用同一个方法，产生不同的结果
animal_sound(dog)  # 输出: 汪汪汪！
animal_sound(cat)  # 输出: 喵喵喵~

