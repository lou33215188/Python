import random
legal_x = [0, 10]
legal_y = [0, 10]


class Turtle:
    __name = "乌龟"

    def __init__(self):
        self.point = 100
        self.x = random.randint(legal_x[0], legal_x[1])
        self.y = random.randint(legal_y[0], legal_y[1])

    def move(self):
        new_x = self.x + random.choice([-2, -1, 1, 2])
        new_y = self.y + random.choice([-2, -1, 1, 2])
        if new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        elif new_x < legal_x[0]:
            self.x = legal_x[0] + (legal_x[0] - new_x)
        else:
            self.x = new_x
        if new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        elif new_y < legal_y[0]:
            self.y = legal_y[0] + (legal_y[0] - new_y)
        else:
            self.y = new_y
        self.point -= 1

    def eat(self):
        self.point += 20


class Fish:
    __name = "鱼"

    def __init__(self):
        self.x = random.randint(legal_x[0], legal_x[1])
        self.y = random.randint(legal_y[0], legal_y[1])

    def move(self):
        new_x = self.x + random.choice([-1, 1])
        new_y = self.y + random.choice([-1, 1])
        if new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        elif new_x < legal_x[0]:
            self.x = legal_x[0] + (legal_x[0] - new_x)
        else:
            self.x = new_x
        if new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        elif new_y < legal_y[0]:
            self.y = legal_y[0] + (legal_y[0] - new_y)
        else:
            self.y = new_y


turtle = Turtle()
fish_ = []
fish_number = 10
for each_number in range(fish_number):
    new_fish = Fish()
    fish_.append(new_fish)
while True:
    if not len(fish_):
        print("鱼都被吃光了，游戏结束！")
        break
    if not turtle.point:
        print("乌龟没有体力了，游戏结束！")
        break
    for each_fish in fish_:
        each_fish.move()
    turtle.move()
    for each_fish in fish_:
        if each_fish.x == turtle.x and each_fish.y == turtle.y:
            turtle.eat()
            print("乌龟吃掉了一条鱼")
            fish_.remove(each_fish)
            print("还有%d条鱼" % len(fish_))
            print("乌龟还有体力：%d " % turtle.point)
