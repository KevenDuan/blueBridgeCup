import sys
from functools import lru_cache
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
mod = 10**9 + 7
ans = 0
lru_cache(maxsize=None) # 记忆化搜索
def dfs(a, b, e):
    global ans
    if a == n and b == m - 1 and e == 1:
        ans += 1
        return
    if e <= 0 and a != n: return # 如果酒已经没了，但是还有花，则不合法
    if a < n: dfs(a+1, b, e*2) # 遇到了店
    if b < m: dfs(a, b+1, e-1) # 遇到了花

dfs(0, 0, 2)
print(ans % mod)