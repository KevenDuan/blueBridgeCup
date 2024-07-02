n,x = map(int,input().split())
a = [0] + list(map(int,input().split()))
Mod = 998244353
dp = [[0] * (64) for _ in range(n + 1)]
# 初始化为 0
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(64):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j ^ a[i]]) % Mod
print(dp[n][x])