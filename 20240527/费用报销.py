from datetime import datetime
from datetime import timedelta
N, M, K = map(int, input().split())
start = datetime(2023, 1, 1)
dp = [[0] * 5010 for _ in range(1010)]
a = [()] # day, value
for _ in range(N):
    m, d, v = map(int, input().split())
    t = datetime(2023, m, d) - start + timedelta(days = 1)
    a.append((t.days, v))
a.sort()
lst = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, N):
        if a[j][0] + K <= a[i][0]:
            lst[i] = j

for i in range(1, N + 1):
    for j in range(5000, a[i][1] - 1, -1):
        dp[i][j] = max(dp[i - 1][j], dp[lst[i]][j - a[i][1]] + a[i][1])
        
print(dp[N][M])