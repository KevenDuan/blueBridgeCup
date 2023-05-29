n, v = map(int, input().split())
N = 3011
c = [0] * N
w = [0] * N
dp = [[0] * N for i in range(N)]

for i in range(1, n + 1):
    c[i], w[i] = map(int, input().split())
    for j in range(0, v + 1):
        if j < c[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j-c[i]]+w[i], dp[i-1][j])

print(dp[n][v])
