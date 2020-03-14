from math import *

H = int(input())
A = int(input())
B = int(input())

if H < B or A < 0.0 or B < 0.0 or H < 0.0 or A > 100.0 or B > 100.0 or H > 100.0:
    print("Wrong Format")
else:
    print((H - 2.0 * B + A - 1.0) // (A - B))
