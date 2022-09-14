class Human:
    def __init__(self, n, a, x):
        self.n = n
        self.a = a
        self.x = x
        
    def who(self):
        print('이름:',self.n, ', 나이:',self.a,', 성별:', self.x)

areum = Human("조아름", 25, "여자")
areum.who()