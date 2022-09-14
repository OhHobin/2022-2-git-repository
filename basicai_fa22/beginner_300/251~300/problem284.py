class 차:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class 자전차(차):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

bicycle = 자전차(2, 100, '시마노')
print(bicycle.z)