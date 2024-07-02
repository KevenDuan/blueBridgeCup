def get_prem(n):
    flag = [0] * (n + 1)
    prem = []
    for i in range(2, n + 1):
        if flag[i] == 0:
            for j in range(i * i, n + 1, i):
                flag[j] = 1
    
    for i in range(2, n + 1):
        if flag[i] == 0: prem.append(i)
    
    return prem

prem = get_prem(1010)
prem.append(1)

for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    
    for i in range(1, n + 1):
        a[i] = a[i - 1] + a[i]

    ans = 0x3f3f3f3f
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            if a[r] - a[l - 1] not in prem:
                ans = min(ans, r - l)
    if ans == 0x3f3f3f3f: print(-1)
    else: print(ans)