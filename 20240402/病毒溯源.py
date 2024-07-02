import sys
sys.setrecursionlimit(10**5)
n = int(input())
G = [[] for _ in range(n)]
st = [0] * n
for _ in range(n):
    tmp = list(map(int, input().split()))[1:]
    G[_].extend(tmp)
    for __ in tmp:
        st[__] = 1
        G[__].append(_)

dp = [1] * (n + 1)
vis = [[_] for _ in range(n)]

for _ in range(n):
    if st[_] == 0:
        root = _

def getMax(n, fa):
    tmp = []
    for s in G[n]:
        if s == fa: continue
        v, li = getMax(s, n)     
        if dp[n] < v+1:
            dp[n] = v + 1
            tmp = li
        elif dp[n] == v+1 and tmp[0] > li[0]:
            dp[n] = v + 1
            tmp = li
    vis[n].extend(tmp) 
    return dp[n], vis[n]

lenth, path = getMax(root, -1)
print(lenth)
print(*path)