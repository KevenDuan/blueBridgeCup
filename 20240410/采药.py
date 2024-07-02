T, M = map(int, input().split())
a = [[0]]
for _ in range(M): a.append(list(map(int, input().split())))
dp = [[0] * (1001) for _ in range(101)]
for i in range(1, M+1):
    for j in range(0, T+1):
        if j >= a[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i][0]] + a[i][1])
        else: dp[i][j] = dp[i-1][j]
print(dp[M][T])