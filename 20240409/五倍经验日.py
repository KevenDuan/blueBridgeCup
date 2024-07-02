n, x = map(int, input().split())
a = [[]]
dp = [[0] * (1001) for _ in range(1001)]
for _ in range(n):
    a.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    for j in range(0, x+1):
        l, w, u = a[i]
        print(l, w)
        if j >= u:
            dp[i][j] = max(dp[i-1][j] + l, dp[i-1][j-u] + w)
        else:
            dp[i][j] = dp[i-1][j] + l

print(dp[n][x] * 5)