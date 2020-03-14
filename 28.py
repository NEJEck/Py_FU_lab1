from math import *

a = int(input())
b = int(input())
c = int(input())
if a < 1000 and b < 1000 and c < 1000:
    pr = ((a + 1) // 2 + (b + 1) // 2 + (c + 1) // 2)
    print(pr)
