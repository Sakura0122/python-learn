class Student:
    name = 'Student'
    def __init__(self):
        print('__init__')

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls)

    def __str__(self):
        print('__str')
        return 'Student object'

    def __repr__(self):
        # 这个返回值清晰地表达了对象的创建方式
        return f"Student('{self.name}', {self.age})"

    def __getattribute__(self, item):
        print('__getattribute__')
        return super().__getattribute__(item)

s1 = Student()
print(s1)
print(s1.name)
