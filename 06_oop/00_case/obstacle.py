from birds import Birds, RedBird, YellowBird


class Obstacle:
    """
        障碍物
    """

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def be_attacked(self, bird: Birds):
        print(f"{bird.name}冲向了{self.name}")

        bird.use_skill()

        if isinstance(bird, RedBird):
            damage = 80
        elif isinstance(bird, YellowBird):
            damage = 70
        else:
            print("类型错误")

        self.strength -= damage

        if self.strength <= 0:
            print(f"{self.name}被摧毁了")
        else:
            print(f"{self.name}被{bird.name}造成了{damage}伤害")

red_bird = RedBird("小红","红色","火焰冲击")
yellow_bird = YellowBird("小黄","黄色","艳阳冲击")

obs1 = Obstacle("木桩",100)
obs2 = Obstacle("石头",200)
obs3 = Obstacle("深坑",300)

obs1.be_attacked(red_bird)
obs1.be_attacked(yellow_bird)
obs1.be_attacked(red_bird)
