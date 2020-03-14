from math import *

N = int(input())
if 100 < N < 999:
    print(N // 100 + N % 100 // 10 + N % 100 % 10)
