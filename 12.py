from math import *
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))
b = sqrt(((x2 - x3) * (x2 - x3)) + ((y2 - y3) * (y2 - y3)))
c = sqrt(((x3 - x1) * (x3 - x1)) + ((y3 - y1) * (y3 - y1)))
P = a + b + c
print(P)
S = P / 2.0
print(sqrt(S * (S - a) * (S - b) * (S - c)))
