from itertools import combinations
import sys
n, m, k = map(int, input().split())

ans = (1<<m) - 1

a = [0]
for _ in range(n):
    tmp = list(set([*map(int, input().split())]))
    tmp_val = 0
    for i in tmp:
        tmp_val = tmp_val|1<<i-1
    a.append(tmp_val)

dp = [0x3f3f3f3f] * (1<<20)
dp[0] = 0
for i in range(1, n+1):
    for j in range(0, 1<<m):
        dp[j] = min(dp[j], dp[j & (~a[i])] + 1)

if dp[ans] == 0x3f3f3f3f: print(-1)
else: print(dp[ans])
