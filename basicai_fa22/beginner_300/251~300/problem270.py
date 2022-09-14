class Stock:
    def __init__(self, n, c, PER, PBR, 배당수익률):
        self.n = n
        self.c = c
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률
    
    def set_name(self, n):
        self.n = n

    def set_code(self, c):
        self.c = c
    
    def get_name(self):
        print(self.n)
    
    def get_code(self):
        print(self.c)

    def set_per(self, PER):
        self.PER = PER

    def set_pbr(self, PBR):
        self.PBR = PBR

    def set_dividend(self, 배당수익률):
        self.배당수익률 = 배당수익률

x = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

x.append(삼성)
x.append(현대차)
x.append(LG전자)

for i in range(len(x)):
    print(x[i].c, x[i].PER)