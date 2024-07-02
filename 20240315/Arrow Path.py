import sys
from functools import lru_cache
sys.setrecursionlimit(10**5)
t = int(input())
for _ in range(t):
    n = int(input())
    Map = [list(input()) for i in range(2)]
    vis = [[0] * (n + 1) for i in range(2)]
    flag = False
    @lru_cache(maxsize = None)
    def dfs(x, y):
        global flag
        vis[x][y] = 1
        if x == 1 and y == n-1:
            flag = True
            return
        for x1, y1 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            xn, yn = x + x1, y + y1
            if xn < 0 or yn < 0 or xn >= 2 or yn >= n: continue
            if vis[xn][yn]: continue
            vis[xn][yn] = 1
            if Map[xn][yn] == '>':
                if yn+1 < n: dfs(xn, yn+1)
            elif Map[xn][yn] == '<':
                if xn+1 < 2: dfs(xn, yn-1)
            vis[xn][yn] = 0
        vis[x][y] = 0

    dfs(0, 0)
    if flag: print('YES')
    else: print('NO')
