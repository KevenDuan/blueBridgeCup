n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
dp = [[0] * (m+1) for i in range(2)]
old = 1
new = 0
for i in range(1, n+1):
    old, new = new, old
    for j in range(1, m+1):
        if a[i] == b[j]:
            dp[new][j] = dp[old][j-1] + 1
        else: dp[new][j] = max(dp[old][j], dp[new][j-1])
            
print(dp[new][m])
