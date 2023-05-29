a, b = map(int, input().split())
N = 10010
dp = [[0] * N for i in range(2)]
for i in range(2):
    for j in range(1, N):
        if i == 0:
            if j < a: dp[i][j] = 0
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-a]+a)
        if i == 1:
            if j < b: dp[i][j] = dp[i-1][j]
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-b]+b)

ans = 0
for i in range(1, N):
    if dp[1][i] != i:
        ans = i
        
print(ans)
