import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def dfs(u, fa, x):
    global res
    ud = 1
    for v in G[u]:
        if v == fa: continue
        ud += dfs(v, u, x)
    if ud >= x:
        ud = 0
        res += 1   
    return ud

def check(x):
    global res
    res = 0
    dfs(1, 0, x)
    return res > k

for __ in range(int(input())):
    n, k = map(int, input().split())
    G = [[] for i in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    l, r = 0, 10**5+1
    while l + 1 != r:
        mid = (l + r) // 2
        if check(mid): l = mid
        else: r = mid

    print(l)
