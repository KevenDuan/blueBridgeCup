cnt = 0
vis = [[1] * 7 for _ in range(7)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(x, y):
    global cnt
    if x == 0 or x == 6 or y == 0 or y == 6:
        cnt += 1
        return
    # 当前点和对称点都已访问
    vis[x][y], vis[6 - x][6 - y] = 0, 0
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        # if nx < 0 or nx > 6 or ny < 0 or ny > 6: continue
        if 0 <= nx <= 6 and 0 <= ny <= 6 and vis[nx][ny] == 1:
            dfs(nx,ny)
    vis[x][y], vis[6 - x][6 - y] = 1, 1
    
dfs(3, 3)
print(cnt // 4)
        
