import sys
# 设置递归深度
sys.setrecursionlimit(60000)

def dfs(i, j):
    global flag
    global arr1
    global arr2
    arr2[i][j] = 1 # 已经被查过
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    if arr1[i + 1][j] == '#' and arr1[i - 1][j] == '#' \
       and arr1[i][j + 1] == '#' and arr1[i][j - 1] == '#':
        flag = 1 # 确定点i，j不会被淹没
    for k in range(4):
        dx = i + d[k][0]
        dy = j + d[k][1]
        # 继续连通搜索没有搜过的点
        if arr2[dx][dy] == 0 and arr1[dx][dy] == '#': dfs(dx, dy)

ans = 0
flag = 0
arr1 = []
n = int(input())
for i in range(n):
    arr1.append(list(input()))
# 已经查询的陆地
arr2 = [[0] * n for i in range(n)]   
    
for i in range(n):
    for j in range(n):
        if arr1[i][j] == '#' and arr2[i][j] == 0:
            flag = 0
            dfs(i, j)
            if flag == 0: ans += 1

print(ans)
