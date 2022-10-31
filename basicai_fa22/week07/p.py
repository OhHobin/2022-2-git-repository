# 파이썬 문제 X
# numpy 손코딩
# sigmoid(x) 미분 전개
# 계산문제(log 계산은 없음)

# 와인 분류 toy project 
# 정확도는 정답이랑 나오는 값이랑 비교해서
# 맞으면 count + 1 해서 정확도 측정
import numpy as np

a = ['1', '2', '3']
x = np.array(a, dtype= np.uint8)
print(x)
print(x.dtype)