n = int(input())
mod = 1000000007
f = [[0] * (4) for _ in range(n+1)]
f[0][0] = 1
for i in range(1, n+1):
    for j in range(4):
        if i < 2 and j > 0: break
        if i < 3 and j > 1: break
        if j == 0:
            for k in range(4):
                f[i][j] = max(f[i][j], f[i-1][k])
        if j == 2:
            for k in range(4):
                f[i][j] = max(f[i][j], f[i-2][k])
        if j >= 3:
            for k in range(4):
                f[i][j] = max(f[i][j], f[i-3][k])

cnt = 0
for i in range(1, n+1):
    for j in range(4):
        if f[i][j]:
            cnt += 1
            cnt = cnt % mod
print(cnt)