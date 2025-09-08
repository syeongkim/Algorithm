month, day = map(int, input().split())

monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

days = day - 1
for i in range(month - 1):
    days += monthList[i]

print(dayList[days % 7])