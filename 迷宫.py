def dfs(x, y, a, i):
    if x < 0 or x > len(data) - 1 or y < 0 or y > len(data[0]) - 1: return
    elif data[x][y] == '1': return
    # 上锁
    data[x][y] = '1'
    a += i
    if x == len(data) - 1 and y == len(data[0]) - 1:
        print(a)
        print()
    for i in dire:
        if i == 'D':
            dfs(x+1, y, a, i)
        if i == 'L':
            dfs(x, y-1, a, i)
        if i == 'R':
            dfs(x, y+1, a, i)
        if i == 'U':
            dfs(x-1, y, a, i)
    # 解锁
    data[x][y] = '0'

data = [[''] * 6 for i in range(4)]
for i in range(4):
    data[i] = list(input())

ans = ''
dire = ['D', 'L', 'R', 'U']
dfs(0, 0, ans, '')

