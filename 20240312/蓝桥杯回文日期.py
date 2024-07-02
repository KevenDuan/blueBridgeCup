import datetime
t = input()
t = datetime.date(int(t[:4]), int(t[4:6]), int(t[6:]))
deta = datetime.timedelta(days = 1)
a1, a2 = 0, 0
while not a1 or not a2:
    t += deta
    s = ''.join(str(t).split('-'))
    if s[::-1] == s:
        if a1 == 0: a1 = s
        if s[0] != s[1] and s[:2] == s[2:4] and s[4:6] == s[6:]: a2 = s
print(f'{a1}\n{a2}')

