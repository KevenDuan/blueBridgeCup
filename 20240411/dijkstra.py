from queue import PriorityQueue
inf = 10**9 + 10
n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    G[x].append([y, z])
    
def dijkstra():
    q = PriorityQueue()
    vis = [0] * (n + 1)
    r = [inf] * (n + 1)
    r[1] = 0
    q.put([r[1], 1])
    while q.qsize() != 0:
        d, v = q.get()
        if vis[v]: continue
        vis[v] = 1 # flag shortest road
        for node, distance in G[v]:
            if vis[node]: continue
            r[node] = min(r[node], distance + d)
            q.put([r[node], node])
    return r

r = dijkstra()
ans = r[n]
if ans > 10**9: print(-1)
else: print(ans)