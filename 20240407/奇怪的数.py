n, m = map(int, input().split())
mod = 998244353
ji = [1, 3, 5, 7, 9]
ou = [0, 2, 4, 6, 8]
ans = 0
def dfs(now, path):
    global ans
    if now == n:
        if sum(sorted(path, reverse=True)[:5]) <= m:
            ans += 1
        return
    
    if len(path) >= 5:
        if sum(sorted(path, reverse=True)[:5]) > m:
            return
    
    if (now+1)&1:
        for i in ji: dfs(now+1, path + [i])
    else:
        for i in ou: dfs(now+1, path + [i])

dfs(0, [])
print(ans % mod)