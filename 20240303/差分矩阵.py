n, m, q = map(int, input().split())
Map = [[0] * (m + 2)]
for i in range(n):
    Map.append([0] + list(map(int, input().split())))

diff = [[0] * (m + 2) for i in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        diff[i][j] = Map[i][j] - Map[i - 1][j] - Map[i][j - 1] + Map[i - 1][j - 1]

for _ in range(q):
    x1, y1, x2, y2, c = map(int, input().split())
    diff[x1][y1] += c
    diff[x2 + 1][y2 + 1] += c
    diff[x1][y2 + 1] -= c
    diff[x2 + 1][y1] -= c

a = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = diff[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]

for i in range(1, n + 1):
    print(*a[i][1:])