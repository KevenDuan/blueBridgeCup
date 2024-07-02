n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(); N = 100000
dp = [0] * N
dp[0] = 1
for i in range(a[0], N):
    for j in a:
        dp[i] = max(dp[i], dp[i-j])
ans = 0
for i in range(N):
    if dp[i] == 0:
        ans += 1
if ans > N//2:print('INF')
else: print(ans)
