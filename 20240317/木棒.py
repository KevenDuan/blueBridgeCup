while True:
    n = int(input())
    if n == 0: break
    a = [*map(int, input().split())]
    a.sort(reverse = True)
    all_sum = sum(a)

    def dfs(u, p, now_len):
        if u * ans == all_sum: return True
        if now_len == ans: # 找到第u个木棒,往后找
            return dfs(u+1, 0, 0)
        
        for i in range(p, n):
            if vis[i]: continue
            if a[i] + now_len > ans: continue
            vis[i] = True
            if dfs(u, i + 1, now_len + a[i]): return True
            vis[i] = False

            if not now_len: return False
            if now_len + a[i] == ans: return False
        
        return False

    vis = [0] * (n + 1)
    ans = 1
    while True:
        flag = False
        if all_sum % ans == 0 and dfs(0, 0, 0):
            print(ans)
            break
        else: ans += 1

