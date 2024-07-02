N, M, K = map(int, input().split())
Map = [[0] * (M + 1)]
for _ in range(N):
    Map.append([0] + list(map(int, input().split())))
prex = [[0] * (M + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prex[i][j] = prex[i - 1][j] + prex[i][j - 1] + Map[i][j] - prex[i - 1][j - 1]

def query(x1, y1, x2, y2):
    return prex[x2][y2] + prex[x1 - 1][y1 - 1] - prex[x2][y1 - 1] - prex[x1 - 1][y2] > K

ans = 0
for y1 in range(1, M + 1):
    for y2 in range(y1, M + 1):
        x1 = 1
        for x2 in range(1, N + 1):
            while x1 <= x2 and query(x1, y1, x2, y2): x1 += 1
            if x1 <= x2: ans += x2 - x1 + 1
print(ans)