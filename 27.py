from math import *

N = int(input())
if 0 < N < 10000:
    print(N + 2 - N % 2)
