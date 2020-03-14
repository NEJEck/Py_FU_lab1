from math import *

A = int(input())
B = int(input())
N = int(input())
if 0 < A < 10000 and 0 < B < 10000 and 0 < N < 10000:
    print((A * N * 100 + B * N) // 100, B * N % 100, sep=" : ")
