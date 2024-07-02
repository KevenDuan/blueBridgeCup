dp = [[-10**18] * 11 for _ in range(10**5 + 1)]
g = [0] * (10**5 + 1)
n, m, k = map(int, input().split())
for i in range(1, n + 1):
    g[i] = [0] + list(map(int, input().split()))
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(0, m + 1):
        dp[i][j] = dp[i - 1][j]
    for j in range(1, m + 1):
        if g[i][j] != -1:
            dp[i][0] = max(dp[i][j] + g[i][j], dp[i][0])
    for j in range(1, m + 1):
        if g[i][j] != -1:
            dp[i][j] = max(dp[i][0] - g[i][j], dp[i][j])
print(dp[n][0] * k)