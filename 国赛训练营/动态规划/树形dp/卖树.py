import sys
sys.setrecursionlimit(10**5)

def dfs(u, f, d):
    dep[u] = d
    for v in G[u]:
        if v == f: continue
        dfs(v, u, d + 1)
        dp[u] = max(dp[u], dp[v] + 1)
        
def dfs2(u, f):
    global ans
    tmpf, mx1, mx2 = 0, 0, 0
    for v in G[u]:
        tmpf = max(tmpf, dp[v] + 1)
    # 维护答案    
    ans = max(ans, tmpf * k - dep[u] * c)
    
    pre = dp[u]
    
    for v in G[u]:
        if dp[v] + 1 > mx1:
            mx2 = mx1
            mx1 = dp[v] + 1
        elif dp[v] + 1 > mx2:
            mx2 = dp[v] + 1
    
    for v in G[u]:
        if v == f: continue
        if dp[v] + 1 == mx1:
            dp[u] = mx2
        else: dp[u] = mx1
        
        dfs2(v, u)
        
    dp[u] = pre

for _ in range(int(input())):
    n, k, c = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        
    dep = [0] * (n + 1) # 以1结点为根的深度
    dp = [0] * (n + 1) # dpi表示以i为根的最大路径长度
    ans = 0 # 存最大的盈利

    dfs(1, 0, 0)
    dfs2(1, 0)
    print(ans)