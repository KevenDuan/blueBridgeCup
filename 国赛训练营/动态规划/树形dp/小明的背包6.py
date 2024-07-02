N, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
w = [0] * (N + 1)
v = [0] * (N + 1)
for _ in range(1, N + 1):
    w_, v_, s_ = map(int, input().split())
    G[s_].append(_)
    w[_], v[_] = w_, v_

dp = [[0] * (V + 1) for _ in range(N + 1)]

def dfs(u):
    for i in range(w[u], V+1):
        dp[u][i] = v[u]
        
    for i in G[u]:
        dfs(i)
        for j in range(V, w[u] + w[i] -1, -1):
            for k in range(w[i], j - w[u] + 1):
                dp[u][j] = max(dp[u][j], dp[u][j - k] + dp[i][k])

dfs(0)
print(dp[0][V])