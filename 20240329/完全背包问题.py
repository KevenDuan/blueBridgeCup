n, v = map(int, input().split())
vi, wi = [0], [0]
for _ in range(n):
    __, ___ = map(int, input().split())
    vi.append(__)
    wi.append(___)

dp = [[0] * (v+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1, v+1):
        if j >= vi[i]:
            dp[i][j] = max(dp[i][j], dp[i][j-vi[i]] + wi[i])
        dp[i][j] = max(dp[i-1][j], dp[i][j])

print(dp[n][v])
