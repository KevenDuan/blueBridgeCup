n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
print(dp[n][n])