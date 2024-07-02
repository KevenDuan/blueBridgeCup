t = int(input())
for _ in range(t):
    n, K = map(int, input().split())
    a = list(map(int, input().split()))
    a1, a2 = a[:n], a[n:]
    d1, d2 = {}, {}
    for i in a1:
        if i in d1:
            d1[i] += 1
        else: d1[i] = 1
    for i in a2:
        if i in d2:
            d2[i] += 1
        else: d2[i] = 1

    t1, t2 = [], []
    for k, v in d1.items():
        t1.append([v, k])
    for k, v in d2.items():
        t2.append([v, k])
    t1.sort(reverse=True); t2.sort(reverse=True)

    cnt = 0
    ans1, ans2 = [], []
    for i in range(len(t1)):
        if cnt >= 2 * K: break
        if t1[i][0] == 2:
            cnt += 2
            ans1.append(t1[i][1])
            ans1.append(t1[i][1])
        else:
            cnt += 1
            ans1.append(t1[i][1])
            ans2.append(t1[i][1])
        if t2[i][0] == 2:
            ans2.append(t2[i][1])
            ans2.append(t2[i][1])
        
    print(*ans1)
    print(*ans2)





        

