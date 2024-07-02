t = int(input())
for c in range(1, t + 1):
    n = int(input())
    Map = [list(input()) for _ in range(n)]
    vis = [[0] * (n + 1) for _ in range(n)]
    def check(x, y, tag):
        cnt = 0
        for x1, y1 in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            xn, yn = x + x1, y + y1
            if xn < 0 or xn >= n or yn < 0 or yn >= n: continue
            if Map[xn][yn] == tag: cnt += 1
        return cnt

    def dfs(x, y):
        vis[x][y] = 1
        for x1, y1 in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            xn, yn = x + x1, y + y1
            if xn < 0 or xn >= n or yn < 0 or yn >= n: continue
            if vis[xn][yn] or Map[xn][yn] == '*': continue
            if Map[xn][yn] == 0:
                dfs(xn, yn)

    for i in range(n):
        for j in range(n):
            if Map[i][j] != '*': Map[i][j] = check(i, j, '*')

    res = 0
    for i in range(n):
        for j in range(n):
            if Map[i][j] == 0 and vis[i][j] == 0:
                res += 1
                dfs(i, j)

    for i in range(n):
        for j in range(n):
            if Map[i][j] != '*' and Map[i][j] != 0 and check(i, j, 0) == 0:
                res += 1

    print(f'Case #{c}: {res}')
                
