def dfs(sta, end):
    if sta == end:
        print(li[0 : end + 1])
    else:
        for i in range(sta, end + 1):
            li[sta], li[i] = li[i], li[sta]
            dfs(sta + 1, end)
            li[i], li[sta] = li[sta], li[i]

li = [i for i in range(1, 10)]
dfs(0, 2)
