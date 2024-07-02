a, b, n = map(int, input().split())
"""
# 暴力法：过50%
day = 0
while n > 0:
    for i in range(7):
        if i >= 5:
            n -= b
        else:
            n -= a
        day += 1
        if n <= 0:
            break
"""
# 过100%
week_work = a * 5 + b * 2
week_day = n // week_work
remain_day = n % week_work
day = week_day * 7
while remain_day > 0:
    for i in range(7):
        if i >= 5:
            remain_day -= b
        else:
            remain_day -= a
        day += 1
        if remain_day <= 0:
            break
print(day)
