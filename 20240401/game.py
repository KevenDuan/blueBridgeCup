n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().split())))

N = 110
dp = [[0] * N for _ in range(N)]
for lenth in range(1, n+1):
    for i in range(n - lenth + 1):
        j = i + lenth - 1
        dp[i][j] = max(a[i] - dp[i+1][j], a[j] - dp[i][j-1])

s = sum(a)
print(f"{(s + dp[0][n-1])//2} {(s - dp[0][n-1])//2}")
