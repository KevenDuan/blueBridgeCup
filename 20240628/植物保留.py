n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 1

for j in range(n):
    cnt = 1
    dis = a[j] + m
    for i in range(j + 1, n):
        if a[i] >= dis:
            cnt += 1
            dis += m
        else: continue
    ans = max(ans, cnt)
print(ans)