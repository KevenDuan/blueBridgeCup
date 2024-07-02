from collections import deque
import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
Map = [list(input()) for _ in range(n)]
ans = 101
def dfs(x, y, tag):
    vis[x][y] = 1
    Map[x][y] = tag
    for x1, y1 in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        xn, yn =  x + x1, y + y1
        if xn < 0 or yn < 0 or xn >= n or yn >= m: continue
        if vis[xn][yn] or Map[xn][yn] == '.': continue
        dfs(xn, yn, tag)

def bfs(x, y):
    global ans
    path = [[0] * (m + 1) for i in range(n + 1)]
    dq = deque()
    dq.append([x, y, 0])
    path[x][y] = 1
    while len(dq) > 0:
        x, y, cnt = dq.popleft()
        if Map[x][y] == 2:
            ans = min(ans, cnt)
            break
        for x1, y1 in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            xn, yn =  x + x1, y + y1
            if xn < 0 or yn < 0 or xn >= n or yn >= m: continue
            if path[xn][yn] == 1 or Map[xn][yn] == 1: continue
            path[xn][yn] = 1
            dq.append([xn, yn, cnt + 1])

flag = 0
vis = [[0] * (m + 1) for i in range(n + 1)]
for i in range(n):
    for j in range(m):
        if Map[i][j] == 'X' and not flag:
            flag = 1
            dfs(i, j, 1)
        elif Map[i][j] == 'X' and flag:
            dfs(i, j, 2)
            break
    
for i in range(n):
    for j in range(m):
        if Map[i][j] == 1:
            bfs(i, j)

print(ans-1)
