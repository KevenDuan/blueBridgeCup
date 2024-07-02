n = int(input())
x = [0] + list(map(int, input().split()))
op = [[]]
for _ in range(n - 1):
    op.append(list(map(int, input().split())))
op.append([0, 0])
dp = [[0] * 2 for i in range(n + 1)]
dp[1][0] = x[1] # init dp
dp[1][1] = x[1] + op[1][0]/0.7
for i in range(2, n + 1):
    dp[i][0] = min(dp[i-1][0] + x[i] - x[i-1], dp[i-1][1] + op[i-1][1]/1.3)
    dp[i][1] = min(dp[i][0] + op[i][0]/0.7, dp[i-1][1] + \
                   abs(op[i-1][1] - op[i][0]) / (1.3 if op[i-1][1] >= op[i][0] else 0.7))
print("%.2f" % dp[n][0])
