idx = 0
w = [0] * 40003
v = [0] * 40003
N, V = map(int, input().split())
dp = [0] * 2003

for _ in range(N):
    ww, vv, c = map(int, input().split())
    if c == 0:
        c = V // ww
    cnt = 1
    while c > cnt:
        idx += 1
        c -= cnt
        w[idx] = cnt * ww
        v[idx] = cnt * vv
        cnt *= 2
    idx += 1
    w[idx] = c * ww
    v[idx] = c * vv

for i in range(1, idx + 1):
    for j in range(V, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(dp[V])