from queue import PriorityQueue

def dijkstra(a, b):
    pq = PriorityQueue()
    r = [0x3f3f3f3f] * (n + 1)
    vis = [0] * (n + 1)
    r[a] = timeout[a]
    pq.put((r[a], a))
    while pq.qsize() != 0:
        val, u = pq.get()
        if vis[u] == 1: continue
        vis[u] = 1 # 标记已经为最优的结点
        for v in G[u]:
            if vis[v] == 1: continue
            r[v] = min(r[v], val + timeout[v])
            pq.put((r[v], v))
    return r[b]
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split()) 
        G[u].append(v)
        G[v].append(u)

    # 记录每个电脑的延迟
    timeout = [0] * (n + 1)
    for i in range(1, n + 1):
        timeout[i] = len(G[i])

    for _ in range(m):
        a, b = map(int, input().split())
        print(dijkstra(a, b))
        