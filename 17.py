from math import *
xA = int(input())
yA = int(input())
xC = int(input())
yC = int(input())
x_diag = (xA + xC) / 2.0
y_diag = (yA + yC) / 2.0
x_vect = xA - x_diag
y_vect = yA - y_diag
xD = x_diag - y_vect
yD = y_diag + x_vect
xB = x_diag + y_vect
yB = y_diag - x_vect
print(xB, yB, sep=' : ')
print(xD, yD, sep=' : ')
