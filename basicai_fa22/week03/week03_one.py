import math

def sol(x):
    f_x = 1/(1+math.exp(-x))
    return f_x * (1 - f_x)

x = int(input('입력: '))
print(sol(x))