n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
dp = [[0] * 4 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = max(dp[i][0], dp[i - 1][2] + a[i])
    dp[i][1] = max(dp[i][1], max(dp[i - 1][0], dp[i - 1][2]) + b[i])
    dp[i][2] = max(dp[i][2], max(dp[i - 1][1], dp[i - 1][3]) + a[i])
    dp[i][3] = max(dp[i][3], dp[i - 1][1] + b[i])

print(max(dp[n]))