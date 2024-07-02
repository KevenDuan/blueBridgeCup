import sys
sys.setrecursionlimit(10**9)
n = int(input())
Map = [list(input()) for _ in range(n)]
vis = [[0] * (n + 1) for _ in range(n + 1)]
def check(x, y):
    for x1, y1 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        xn, yn = x + x1, y + y1
        if xn < 0 or xn >= n or yn < 0 or yn >= n: continue
        if Map[xn][yn] == '.': return False
    return True
    
def dfs(x, y):
    global flag
    vis[x][y] = 1
    for x1, y1 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        xn, yn = x + x1, y + y1
        if xn < 0 or xn >= n or yn < 0 or yn >= n: continue
        if vis[xn][yn] == 0 and Map[xn][yn] == '#':
            if check(xn, yn): flag = True
            dfs(xn, yn)

cnt = 0
for i in range(n):
    for j in range(n):
        if vis[i][j]: continue
        if Map[i][j] == '#':
            flag = False
            cnt += 1
            dfs(i, j)
            if flag: cnt -= 1
print(cnt)

