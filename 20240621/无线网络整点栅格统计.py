def solve(x1, y1, x2, y2):
    x3, y3 = x1 + (y2 - y1), y1 - (x2 - x1)
    x4, y4 = x2 + (y2 - y1), y2 - (x2 - x1)
    if 0 <= x3 <= n and 0 <= x4 <= n and 0 <= y3 <= m and 0 <= y4 <= m:
        arr[x1][y1] += 1

n, m = map(int, input().split())
arr = [[0] * (m + 1) for _ in range(n + 1)]

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for y1 in range(m + 1):
            for y2 in range(m + 1):
                if x1 == x2 and y1 == y2: continue
                solve(x1, y1, x2, y2)

for i in range(len(arr)):
    print(*arr[i])