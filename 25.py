from math import *

N = int(input())
if 0 <= N <= 1000000:
    if N < 10:
        print(0)
    else:
        s = (N // 10) % 10
        print(s)
