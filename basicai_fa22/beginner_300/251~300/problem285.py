class 차:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class 자동차(차):
    def 정보(self):
        print('바퀴수', self.x)
        print('가격', self.y)

car = 자동차(4, 1000)
car.정보()