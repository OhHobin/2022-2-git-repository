import random

class Account:
    def __init__(self, n, b):
        self.n = n
        self.b = b
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

kim = Account("오호빈", 23000)
print(kim.n)
print(kim.b)
print(kim.bank)
print(kim.account_number)