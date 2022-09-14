class Stock:
    def __init__(self, n, c):
        self.n = n
        self.c = c
    
    def set_name(self, n):
        self.n = n

    def set_code(self, c):
        self.c = c
        
삼성 = Stock("삼성전자", "005930")