import random

class Account:
    count = 0
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
        Account.count += 1
    
    def get_account_num(self):
        print(Account.count)
    
    def deposit(self, b):
        if b > 0:
            self.b += b
            print('입금 완료')
        else:
            print('1원 이상만 입금가능합니다')
    
    def withdraw(self, b):
        if b < self.b:
            self.b -= b
            print('출금 완료')
        else:
            print('계좌 잔고 초과입니다.')

oh = Account("오호빈", 23000)
oh.get_account_num()
oh.deposit(10000)
