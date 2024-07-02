import datetime, sys
def solve(t1, t2):
    t1 = datetime.date(int(t1[:4]), int(t1[4:6]), int(t1[6:]))
    t2 = datetime.date(int(t2[:4]), int(t2[4:6]), int(t2[6:]))
    if t1 > t2:
        t1, t2 = t2, t1
    deta = t2 - t1
    print(deta.days + 1)

while True:
    try:
        t1 = input()
        t2 = input()
        solve(t1, t2)
    except:
        break
