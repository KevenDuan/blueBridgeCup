# dfs
def dfs(x, y, c, s):
    if vis[x][y] == 1: return  # 已经搜索过的返回
    if s * 2 == num: ans.append(c)
    vis[x][y] = 1  # 标记为搜索过
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i in d:
        tx = i[0] + x
        ty = i[1] + y
        if tx >= 0 and ty >= 0 and tx <= (n - 1) and ty <= (m - 1):
            if vis[tx][ty] == 0:
                dfs(tx, ty, c + 1, s + data[tx][ty])
    vis[x][y] = 0  # 还原

# 输入
m, n = map(int, input().split())
vis = [[0] * m for i in range(n)]
data = [list(input().split()) for i in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        data[i][j] = int(data[i][j])
        num += data[i][j]
ans = []
dfs(0, 0, 1, data[0][0])
if len(ans) == 0:
    print(0)
else:
    print(min(ans))
