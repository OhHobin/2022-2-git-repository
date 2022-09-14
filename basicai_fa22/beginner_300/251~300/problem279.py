import random

class Account:
    count = 0
    def __init__(self, n, b):
        self.c = 0
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
        self.c += 1
        if self.c % 5 == 0:
            self.b += self.b * 1.01
    
    def withdraw(self, b):
        if b < self.b:
            self.b -= b
            print('출금 완료')
        else:
            print('계좌 잔고 초과입니다.')
    
    def display_info(self):
        print('은행이름:', self.bank )
        print('예금주:',self.n)
        print('계좌번호:', self.account_number)
        print('잔고', self.b)
        

oh = Account("오호빈", 23000)
ooh = Account("오빈", 33000)
oooh = Account("빈", 43000)
oh.get_account_num()
oh.deposit(10000)
oh.display_info()
x = [oh, ooh, oooh]
for i in range(len(x)):
    if x[i].b >= 1000000:
        print(x[i])