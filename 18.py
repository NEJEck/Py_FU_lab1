from math import *
xA = int(input())
yA = int(input())
zA = int(input())
xB = int(input())
yB = int(input())
zB = int(input())
xC = int(input())
yC = int(input())
zC = int(input())
xD = int(input())
yD = int(input())
zD = int(input())
xAB = xB - xA
yAB = yB - yA
zAB = zB - zA
xAC = xC - xA
yAC = yC - yA
zAC = zC - zA
xAD = xD - xA
yAD = yD - yA
zAD = zD - zA
smeshannoeProizvedenie = xAB * yAC * zAD + yAB * zAC * xAD + zAB * xAC * yAD - xAD * yAC * zAB - yAD * zAC * xAB - zAD * xAC * yAB
V = 1/6 * smeshannoeProizvedenie
print(V)



