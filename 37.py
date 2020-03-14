from math import *

A = int(input())
B = int(input())
C = A % B
D = B % A
K = C * D + 1
print(K)   # Если делится нацело output = 1
