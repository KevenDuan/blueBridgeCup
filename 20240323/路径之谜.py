import sys
n = int(input())
cnt = 0
Map = [[0] * n for i in range(n)]
vis = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        Map[i][j] = cnt
        cnt += 1
north = list(map(int, input().split()))
west = list(map(int, input().split()))
def dfs(x, y, path):
    if x == n-1 and y == n-1 and max(north) == max(west) == 0:
        print(*path)
        sys.exit()
    for x1, y1 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        xn, yn = x + x1, y + y1
        if xn < 0 or xn >= n or yn < 0 or yn >= n: continue
        if vis[xn][yn] or north[yn] <= 0 or west[xn] <= 0: continue
        north[yn] -= 1; west[xn] -= 1; vis[xn][yn] = 1
        path.append(Map[xn][yn])
        dfs(xn, yn, path)
        path.pop()
        vis[xn][yn] = 0; north[yn] += 1; west[xn] += 1

vis[0][0] = 1; north[0] -= 1; west[0] -= 1
dfs(0, 0, [0])
