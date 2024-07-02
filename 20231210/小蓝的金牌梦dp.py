n = int(input())
li = [0] + list(map(int, input().split()))

N = int(1e5)
c = []
flag = [True] * (N + 10)
for i in range(2, N):
    for j in range(2, int(N/i) + 1):
        if flag[i * j]: flag[i * j] = False
        else: continue
    if flag[i]: c.append(i)

dp = [0] * (N + 10)
cnt = 0
for i in range(1, len(li)):
    if dp[i - 1] + li[i] > li[i]: cnt += 1
    else: cnt = 1
    dp[i] = max(dp[i - 1] + li[i], li[i])

res = 0
for i in range(N):
    res = max(dp[i], res)

print(dp[:10])
print(cnt)



