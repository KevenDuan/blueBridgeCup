v, n = map(int, input().split())
a = [0] + list(map(int, input().split()))
dp = [0] * (n+5)
dp[0] = 1
for i in range(1, v+1):
    for j in range(1, n+1):
        if j >= a[i]:
            dp[j] += dp[j-a[i]]
print(dp[n])
