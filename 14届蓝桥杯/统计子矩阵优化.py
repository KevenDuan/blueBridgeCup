n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
scnt = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        scnt[i][j] = scnt[i - 1][j] + scnt[i][j - 1] - scnt[i - 1][j - 1] + arr[i - 1][j - 1]

ans = 0
for i1 in range(1, n + 1):
    for i2 in range(i1, n + 1):
        for j1 in range(1, m + 1):
            for j2 in range(j1, m + 1):
                num = scnt[i2][j2] - scnt[i2][j1 - 1] - scnt[i1 - 1][j2] + scnt[i1 - 1][j1 - 1]
                if num <= k:
                    ans += 1

print(ans)
