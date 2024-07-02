def dfs(s, t):
    if s == t:
        print(b[0: n])
    else:
        for i in range(t):
            if not vis[i]:
                vis[i] = True
                b[s] = a[i]
                dfs(s+1, t)
                vis[i] = False

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0] * 10
vis = [False] * 10
n = 3
dfs(0, n)
