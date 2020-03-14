hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
if hour1 > 24 or min1 > 60 or sec1 > 60 or hour2 > 24 or min2 > 60 or sec1 > 60:
    print("Wrong Format")
else:
    time1 = hour1 * 3600 + min1 * 60 + sec1
    time2 = hour2 * 3600 + min2 * 60 + sec2
    continuee = time2 - time1
    if continuee < 0:
        print(continuee / 3600 * (-1), continuee % 3600 / 60 * (-1), continuee % 3600 % 60 * (-1), sep= ' : ')
    else:
        print(continuee / 3600 , continuee % 3600 / 60, continuee % 3600 % 60, sep=' : ')
