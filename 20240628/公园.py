from collections import deque
te, fe, s = map(int, input().split())
t, f, n, m = map(int, input().split())
N = 40010
Map = [[] * N for _ in range(N)]
for _ in range(m):
    x, y = map(int, input().split())
    Map[x].append(y)
    Map[y].append(x)

dis = [[0x3f3f3f3f, 0x3f3f3f3f, 0x3f3f3f3f] for _ in range(N)]

def bfs(sta, idx):
    dq = deque()
    dq.append((sta, 0))
    vis = [0] * N
    while len(dq) != 0:
        nd, val = dq.popleft()
        dis[nd][idx] = val
        vis[nd] = 1
        for v in Map[nd]:
            if vis[v]: continue
            dq.append((v, val + 1))

bfs(t, 0)
bfs(f, 1)
bfs(n, 2)
ans = 0x3f3f3f3f
for i in range(1, n + 1):
    if dis[i][0] + dis[i][1] + dis[i][2] > 1e9: continue
    ans = min(ans, dis[i][0] * te + dis[i][1] * fe + dis[i][2] * (te + fe - s))
if ans > 1e9: print(-1)
else: print(ans)
