n, m, q = map(int, input().split())
a = [[0] * (m + 1)]
for i in range(n):
    a.append([0] + list(map(int, input().split())))

prex = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prex[i][j] = a[i][j] + prex[i][j - 1] + prex[i - 1][j] - prex[i - 1][j - 1]

for _ in range(q):
    x2, y2, x1, y1 = map(int, input().split())
    print(prex[x1][y1] - prex[x1][y2 - 1] - prex[x2 - 1][y1] + prex[x2 - 1][y2 - 1])
