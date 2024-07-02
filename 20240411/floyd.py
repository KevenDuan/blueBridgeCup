inf = 10**9 + 10
n, m = map(int, input().split())
dp = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    dp[x][y] = min(dp[x][y], z)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
ans = dp[1][n]
if ans > 1e9: print(-1)
else: print(ans)