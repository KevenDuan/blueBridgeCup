import sys
n, m, k = map(int, input().split())
mod = 998244353
dp = [[0] * (m+1) for _ in range(n+1)]
if k == 0:
    print(pow(m, n, mod))
    sys.exit()

for j in range(1, m+1):
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(1, m+1):
        dp[i-1][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod
    for j in range(1, m+1):
        if j - k >= 0: dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % mod
        else: dp[i][j] = (dp[i][j] + dp[i-1][m] - dp[i-1][min(m, j+k-1)]) % mod
        dp[i][j] = dp[i][j] % mod

ans = 0
for i in range(1, m+1):
    ans = (ans + dp[n][i]) % mod
print(ans % mod)