n, m = map(int, input().split())
a = [0] + list(input())
b = [0] + list(input())
N = 1010
dp = [[0] * N for _ in range(N)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[n][m])
