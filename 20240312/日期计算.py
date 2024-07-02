from datetime import date, timedelta
y = int(input())
t = date(y, 1, 1) + timedelta(days = int(input()) - 1)
print(f'{int(str(t)[5:7])}\n{int(str(t)[8:])}')
