x, y = map(int, input().split())

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_day = y - 1
for month in range(1, x):
    total_day += day_in_month[month - 1]

day_of_week = total_days % 7

if day_of_week == 0:
    print("MON")
elif day_of_week == 1:
    print("TUE")
elif day_of_week == 2:
    print("WED")
elif day_of_week == 3:
    print("THU")
elif day_of_week == 4:
    print("FRI")
elif day_of_week == 5:
    print("SAT")
else:
    print("SUN")
