import sys
sys.setrecursionlimit(10**5)
n = int(input())
a = [0] + list(map(int, input().split()))
G = [[] for _ in range(n + 1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = 0
dp = [0] * (n + 1)
def dfs(now, fa):
    global ans
    dp[now] = a[now]
    for node in G[now]:
        if node == fa: continue
        dp[node] = dfs(node, now)
        if dp[node] > 0:
            dp[now] += dp[node]
            
    ans = max(ans, dp[now])
    return dp[now]

dfs(1, 0)
print(ans)