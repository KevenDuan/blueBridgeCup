n, m = map(int, input().split())
N = 110; mod = 10**9 + 7
dp = [[[0] * N for i in range(N)] for i in range(N)]
dp[0][0][2] = 1 # 初始化dp
for i in range(n + 1):
    for j in range(m + 1):
        for k in range(m + 1):
            if i == 0 and j == 0: continue
            if i and k % 2 == 0: dp[i][j][k] += dp[i-1][j][k//2] % mod
            if j: dp[i][j][k] += dp[i][j-1][k+1] % mod

print(dp[n][m-1][1] % mod)
print(0%2)