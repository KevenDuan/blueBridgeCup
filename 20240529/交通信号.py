from queue import PriorityQueue
n, m, s, t = map(int, input().split())
G = [[] for _ in range(n + 1)]
inf = 10**18
for _ in range(m):
    u, v, green, r, d = map(int, input().split())
    G[u].append((v, green, r, d, 0)) # 0代表可以正向通过
    G[v].append((u, green, r, d, 1)) # 1代表可以逆向通过

def dijkstra():
    pq = PriorityQueue()
    r = [inf] * (n + 1)
    vis = [0] * (n + 1)
    r[s] = 0
    pq.put((r[s], s)) # 存的是最短时间和结点
    while pq.qsize() != 0:
        dist, u = pq.get()
        if vis[u] == 1: continue
        vis[u] = 1
        for v, green, red, d, tag in G[u]:
            if v == u: continue
            if vis[v] == 1: continue
            T = green + red + 2 * d # 代表一个周期
            wait = 0 # 需要等待的时间
            if tag == 0: # 可以正向通过
                if r[u] % T >= green:
                    wait = T - r[u] % T
            else: # 可以反向通过
                if r[u] % T < green + d:
                    wait = green + d - r[u] % T
                if r[u] % T > green + red + d:
                    wait = T - r[u] % T + green + d
            r[v] = min(r[v], wait + r[u] + d)
            pq.put((r[v], v))
            
    return r[t]

ans = dijkstra()
print(ans if ans != inf else -1)