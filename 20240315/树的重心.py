n = int(input())
g = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(node, fa):
    res = 1
    for i in g[node]:
        if i == fa: continue
        res += dfs(i, node)
    return res

def search(node, fa):
    cnt = 1
    mm = 0
    c = 0x7ffffff
    for i in g[node]:
        if i == fa: continue
        tmp = dfs(i, node)
        cnt += tmp
        mm = max(mm, tmp)
        c = min(c, search(i, node))
    return min(max(mm, n - cnt), c)
print(search(1, 0))
        
