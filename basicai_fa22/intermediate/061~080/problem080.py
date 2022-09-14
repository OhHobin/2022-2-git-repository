from itertools import permutations
from itertools import combinations

import itertools

user_input = input().split(',')
user_input_int = int(input())
print(list(map(''.join, combinations(user_input, user_input_int))))