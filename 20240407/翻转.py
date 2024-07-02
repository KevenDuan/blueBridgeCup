d = int(input())
# d = 1 # test
for _ in range(d):
    t = list(map(int, input()))
    s = list(map(int, input()))
    n = len(t)
    cnt = 0; flag = True
    for i in range(n):
        if t[i] != s[i] and (i == 0 or i == n-1):
            flag = False
            break
        elif t[i] != s[i] and s[i-1] == s[i+1] != s[i]:
            cnt += 1
            if s[i] == 0: s[i] = 1
            else: s[i] = 0
        elif t[i] != s[i]:
            flag = False
            break
    if flag: print(cnt)
    else: print(-1)