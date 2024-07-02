N, K = map(int, input().split())
a = [0]
for i in range(N):
    a.append(int(input()))
prex = [0] * (N + 1)
for i in range(1, N + 1):
    prex[i] = a[i] + prex[i - 1]
for i in range(1, N + 1):
    prex[i] = prex[i] % K

d = {}
for i in range(1, N + 1):
    if prex[i] in d:
        d[prex[i]] += 1
    else: d[prex[i]] = 1

ans = 0
for k, v in d.items():
    if k == 0: ans += v
    ans += v * (v - 1) // 2

print(ans)