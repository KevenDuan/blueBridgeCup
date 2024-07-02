n = int(input())
g = [[] for i in range(n + 1)]
for _ in range(n-1):
    p, q, d = map(int, input().split())
    g[p].append([q, d])
    g[q].append([p, d])

vis = [0] * (n + 1)
def dfs(a, b, path):
    res = -1
    if a == b:
        return path
    for i, d in g[a]:
        if vis[i]: continue
        vis[i] = 1
        res = max(res, dfs(i, b, path + d))
        vis[i] = 0
    return res

ans = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        vis[i] = 1
        ans = max(ans, dfs(i, j, 0))
        vis[i] = 0
print(ans * 10 + (1 + ans) * ans // 2)
        
