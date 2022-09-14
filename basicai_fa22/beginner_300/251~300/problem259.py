class Human:
    def __init__(self, n, a, x):
        self.n = n
        self.a = a
        self.x = x
        
    def who(self):
        print('이름:',self.n, ', 나이:',self.a,', 성별:', self.x)
    
    def setinfo(self, n, a, x):
        self.n = n
        self.a = a
        self.x = x

    def __del__(self):
        print("나의 죽음을 알리지마라")

areum = Human("?", 0, "?")
areum.who()
areum.setinfo("아름", 25, "여자")
areum.who() 
del(areum)