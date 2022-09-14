def bubble(x, y):
	for i in range(x-1):
		for j in range(x-i-1):
			if y[j] > y[j+1]:
				y[j], y[j+1] = y[j+1], y[j]
	for i in range(x):
		print(y[i], end = " ")

x = int(input())
y = list(map(int, input().split()))

bubble(x, y)