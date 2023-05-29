def solve(c, n):
    for i in range(1, n + 1): # 前n件物品
        for j in range(0, c + 1): # 0 ~ V 的容量 
            if w[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
    return dp[n][V]

N = 3011
n, V = map(int, input().split())
dp = [[0] * N for i in range(N)]
w = [0] * N # 体积
v = [0] * N # 价值
for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())
print(solve(V, n))
