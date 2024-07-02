from functools import lru_cache
import sys
sys.setrecursionlimit(10**5)
for __ in range(int(input())):
    n, m, x = map(int, input().split())
    a = []; vis = [0] * (n+1)
    for _ in range(m):
        a.append(list(input().split()))

    def move_1(x, r): return ((x-1)+int(r))%n + 1
    def move_2(x, r): return (n - (int(r)-x+1)) % n + 1

    @lru_cache(maxsize = None)
    def dfs(x, cnt):
        if cnt == m:
            vis[x] = 1
            return
        r, dire = a[cnt][0], a[cnt][1]
        if dire == '0':
            dfs(move_1(x, r), cnt+1)
        elif dire == '1':
            dfs(move_2(x, r), cnt+1)
        else:
            dfs(move_1(x, r), cnt+1)
            dfs(move_2(x, r), cnt+1)

    dfs(x, 0)
    cnt = 0; res = []
    for _ in range(len(vis)):
        if vis[_] == 1:
            cnt += 1
            res.append(_)
    print(cnt)
    print(*res)
