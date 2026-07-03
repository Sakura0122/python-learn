class Birds:
    """
        此类属于 所有鸟类的父类
        属性：名字 颜色 技能描述
    """

    def __init__(self, name, color, skill):
        self.name = name
        self.color = color
        self.skill = skill

    def fly(self):
        print(f"{self.name}在飞行")

    def call(self):
        print(f"{self.name}发出叫声")

    def use_skill(self):
        print(f"{self.name}使用技能")


class RedBird(Birds):
    """
        如果没有额外的单独属性 可以不用书写__init__方法 默认使用父类的
    """

    def fly(self):
        super().fly()
        print(f"{self.name}以稳定的速度飞行")

    def call(self):
        print(f"{self.name}发出ji~ji~ji的叫声")


class YellowBird(Birds):
    """
        黄鸟
    """

    def fly(self):
        super().fly()
        print(f"{self.name}以飞快的速度飞行")

    def call(self):
        super().call()
        print(f"{self.name}发出ga~ga~ga的叫声")
