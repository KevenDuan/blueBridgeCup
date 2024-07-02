def dfs(u, fa):
    dep[u] = dep[fa] + 1
    p[u][0] = fa
    for i in range(1, maxlog):
        p[u][i] = p[p[u][i - 1]][i - 1]
    for v in G[u]:
        if v == fa: continue
        dfs(v, u)

def lca(x, y):
    if dep[x] < dep[y]:
        x, y = y, x
    
    for i in range(maxlog - 1, -1, -1):
        if dep[p[x][i]] >= dep[y]:
            x = p[x][i]
    if x == y: return x
    
    for i in range(maxlog - 1, -1, -1):
        if p[x][i] != p[y][i]:
            x, y = p[x][i], p[y][i]
    return p[x][0]

if __name__ == "__main__":
    n = int(input())
    G = [[] for _ in range(n + 1)]
    dep = [0] * (n + 1)
    maxlog = 21
    p = [[0] * maxlog for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    dfs(1, 0)
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(lca(a, b))