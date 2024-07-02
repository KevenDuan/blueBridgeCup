import datetime
t1 = input()
t2 = input()
t1 = datetime.date(int(t1[:4]), int(t1[4:6]), int(t1[6:]))
t2 = datetime.date(int(t2[:4]), int(t2[4:6]), int(t2[6:]))
date = datetime.timedelta(days=1)
ans = 0
while True:
    s = ''.join(t1.isoformat().split('-'))
    if s[::-1] == s: ans += 1
    if t1 == t2: break
    else: t1 += date
print(ans)
