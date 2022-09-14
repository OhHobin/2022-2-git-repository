class 차:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class 자전차(차):
    pass

bicycle = 자전차(2, 100)
print(bicycle.y)