import sys
sys.setrecursionlimit(60000)
# 构建mp和vis数组
n = int(input())
mp = [[] for _ in range(n)]
for i in range(n):
    mp[i] = list(input())
vis = []
for i in mp:
    vis.append([0] * len(i))
# 方向坐标
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y):
    global flag, mp, vis
    vis[x][y] = 1 # 标记为访问过
    if mp[x + 1][y] == '#' and mp[x - 1][y] == '#' and \
       mp[x][y + 1] == '#' and mp[x][y - 1] == '#': # 判断是否为高地
        flag = 1 # 标记有高地
    for i in dir: # 搜寻四周的点
        nx = x + i[0]
        ny = y + i[1]
        if mp[nx][ny] == '#' and vis[nx][ny] == 0: dfs(nx, ny)
          
flag = 0
ans = 0
for i in range(1, n):
    for j in range(1, n):
        if mp[i][j] == '#' and vis[i][j] == 0:
            flag = 0
            dfs(i, j)
            if flag == 0: ans += 1
print(ans)
