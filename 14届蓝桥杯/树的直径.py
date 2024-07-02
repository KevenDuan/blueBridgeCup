import sys
sys.setrecursionlimit(30000)

def dfs(u, father, d):
    dist[u] = d
    for v, w in edges[u]:
        if v != father:
            dfs(v, u, w + d) 

n = int(input())
dist = [0] * (n + 1) # 记录距离
edges = [[] for i in range(n + 1)]
for i in range(n-1):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
    edges[b].append((a, w))

dfs(1, -1, 0)
s = 1
for i in range(len(dist)):
    if dist[i] > dist[s]:
        s = i

dfs(s, -1, 0)
t = 1
for i in range(len(dist)):
    if dist[i] > dist[t]:
        t = i

print(dist[t])
    
    
