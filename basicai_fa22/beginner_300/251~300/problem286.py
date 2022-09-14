class 차:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class 자전차(차):
    def 정보(self):
        print('바퀴수', self.x)
        print('가격', self.y)

bicycle = 자전차(2, 100, '시마노')
bicycle.정보()