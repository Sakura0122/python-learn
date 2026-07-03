class Person:
    home = 'Earth'

    @classmethod
    def test_method(cls):
        print(cls.home)

    @staticmethod
    def test_static_method():
        print('This is a static method')

Person.test_static_method()
Person.test_method()