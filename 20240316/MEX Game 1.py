t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else: d[i] = 1

    t = []
    for k, v in d.items():
        t.append([v, k])
    t.sort()
    m = 0
    if len(t) >= 2 and t[1][0] >= 2:
        m = t[-1][1] + 1
    elif len(t) >= 2 and t[1][0] == 1:
        m = t[1][1]
    else:
        m = t[0][1] + 1
    flag = True
    for i in range(0, m+1):
        if i not in d:
            print(i)
            flag = False
            break

    if flag: print(m)
