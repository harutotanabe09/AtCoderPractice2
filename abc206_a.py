N = int(input())

money = 0
day = 1
while money < N:
    money += day
    day += 1

print(day-1)
