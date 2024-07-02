# dp滚动半暴力法 过100%
n = int(input())
N = 10010
w = [0]
for i in range(n):
    w.append(int(input()))

w.sort() # 排序
dp = [[0] * N for i in range(2)]
old = 1
new = 0
for i in range(1, n + 1):
    old, new = new, old
    for j in range(1, N):
        if w[i] > j:
            dp[new][j] = dp[old][j]
        else:
            dp[new][j] = max(dp[new][j - w[i]]+w[i], dp[old][j])

ans = 0
for i in range(1, len(dp[1])):
    if i != dp[new][i]:
        ans += 1

if ans > 5500:
    ans = 'INF'

print(ans)
