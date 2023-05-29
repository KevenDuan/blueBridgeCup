n = int(input())
dp = [[0] * n for i in range(n)]
data = [0] * n
for i in range(n):
    data[i] = list(map(int, list(input().split())))

for i in range(1, n):
    for j in range(len(data[i])):
        if i == 1: # 上层只有一个点
            dp[i][j] += data[0][0] + data[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + data[i][j]
        elif j == len(data[i])-1:
            dp[i][j] = dp[i-1][j-1] + data[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + data[i][j]
print(dp)
if n % 2 == 1:
    print(dp[n-1][n//2])
else:
    print(max(dp[n-1][n//2], dp[n-1][n//2 - 1]))
