def tfm(s, i):
    return ord(s[i]) - ord('a')

n = int(input())
a = [0]
for i in range(n): a.append(input())

dp = [[0x3f3f3f3f] * 26 for _ in range(n + 1)]
dp[1][tfm(a[1], 0)] = dp[1][tfm(a[1], 1)] = 2

for i in range(2, n + 1):
    for j in range(26):
        A, B = tfm(a[i], 0), tfm(a[i], 1)
        # 不翻转 'AB'
        if A == j: dp[i][B] = min(dp[i][B], dp[i - 1][j] + 1)
        else: dp[i][B] = min(dp[i][B], dp[i - 1][j] + 2)
        # 翻转的情况 'BA'
        if B == j: dp[i][A] = min(dp[i][A], dp[i - 1][j] + 1)
        else: dp[i][A] = min(dp[i][A], dp[i - 1][j] + 2)
            
ans = 0x3f3f3f3f
for i in range(26):
    ans = min(ans, dp[n][i])
print(ans)