from math import *
p = int(input())
V1 = p / 0.0445 / 16.0 / 3.0 / 500.0
V2 = round(V1 * 100.0) / 100.0
K1 = p / 0.0445 / 16.0 / 3.0
K2 = round(K1 * 100.0) / 100.0
P1 = p / 0.0445 / 16.0
P2 = round(P1 * 100.0) / 100.0
print(V2)
print(K2)
print(P2)
print(p / 0.0445)