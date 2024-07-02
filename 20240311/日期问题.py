import datetime
t = input()
t = list(map(int, [t[:2], t[3:5], t[6:8]]))
ans = []
year = [t[0], t[2]]
for i in range(len(year)): # year
    if i == 0:
        i = year[0]
        j, k = t[1], t[2]
        try:
            if i < 60:
                tt = datetime.date(2000 + i, j, k)
            else: tt = datetime.date(1900 + i, j, k)
            ans.append(tt)
        except: continue
    else: # i == t[2]
        i = year[1]
        for j in [t[0], t[1]]: # month
            if j == t[0]:
                k = t[1]
                # print(i, j, k)
            else: k = t[0]
            try:
                if i < 60:
                    tt = datetime.date(2000 + i, j, k)
                else: tt = datetime.date(1900 + i, j, k)
                ans.append(tt)
            except: continue
ans = sorted(set(ans))
for i in ans:
    print(i)
