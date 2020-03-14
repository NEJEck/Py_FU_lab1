N = int(input())
n1 = N // 1000
n2 = N // 100 % 10
n3 = N // 10 - n1 * 100 - n2 * 10
n4 = N % 10
S1 = (n1 - n4) ** 2
S2 = (n2 - n3) ** 2
print(S1 + S2 + 1)
