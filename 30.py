from math import *

N = int(input())
hours = N // 3600
N -= hours * 3600

minutes = N // 60
N -= minutes * 60
seconds = N

print(hours % 24, end="")
print(' : ', end="")
print(minutes // 10, minutes % 10, end="")
print(' : ', end="")
print(seconds // 10, seconds % 10, end="")
