from math import *

N = int(input())
K = int(input())
if N > 10000 or K > 10000:
    print("Wrong Format")
else:
    print(K // N)
