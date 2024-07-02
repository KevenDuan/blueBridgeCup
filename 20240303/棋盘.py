n, m = map(int, input().split())
a = [[0] * (n + 2) for i in range(n + 2)]
diff = [[0] * (n + 2) for i in range(n + 2)]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    diff[x1][y1] += 1
    diff[x2 + 1][y2 + 1] += 1
    diff[x2 + 1][y1] -= 1
    diff[x1][y2 + 1] -= 1

prex = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prex[i][j] = diff[i][j] + prex[i-1][j] + prex[i][j-1] - prex[i-1][j-1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(prex[i][j]&1, end = '')
    print()