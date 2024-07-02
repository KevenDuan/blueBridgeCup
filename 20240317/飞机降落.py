t = int(input())
for __ in range(t):
    n = int(input())
    a = [[0, 0, 0]]
    for _ in range(n):
        a.append(list(map(int, input().split())))

    flag = False
    def dfs(u, last): # 第u辆飞机, 在last时间段结尾
        global flag
        if u >= n:
            print('YES')
            flag = True
        if flag: return
        
        for i in range(1, n+1):
            if vis[i]: continue
            if a[i][0] + a[i][1] < last: return
            vis[i] = 1
            if last < a[i][0]: dfs(u+1, a[i][0] + a[i][2])
            else: dfs(u+1, last + a[i][2])
            vis[i] = 0

    vis = [0] * (n + 1)
    dfs(0, 0)
    if not flag: print('NO')
