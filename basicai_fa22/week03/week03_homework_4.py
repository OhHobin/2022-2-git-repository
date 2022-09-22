import random

class dice:
    def __init__(self, x, y, size):
        self.vl = []
        self.value = 0
        self.x = x
        self.y = y
        self.size = size
    
    def random_value(self):
        self.value = random.randint(1, 6)
        self.vl.append(self.value)
    
    def get_value_list(self):
        return self.vl

dice_one = dice(20, 30, 100)
print('주사위 위치(x, y):', dice_one.x, dice_one.y)
print('주사위 사이즈:', dice_one.size)
print('주사위 초기값:', dice_one.value)
dice_one.random_value()
print(dice_one.value)