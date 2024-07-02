def gcd(a, b):
    m = max(a, b)
    n = (a + b) - m
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n
    
stack = []
n, m = map(int, input().split())
li = [list(map(int, input().split())) for i in range(n)]
vis = [[0 for i in range(m)] for j in range(n)]
r, c = map(int, input().split())
r -= 1; c -= 1
dire = [(0, -1), (-1, 0), (0, 1), (1, 0)]
cnt = 0
stack.append((r, c))
vis[r][c] = 1 # lock
while len(stack) != 0:
    flag = True
    x1 = stack[-1][0]
    y1 = stack[-1][1]
    for i in dire:
        x2 = x1 + i[0]
        y2 = y1 + i[1]
        if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m: continue
        if vis[x2][y2]: continue
        if gcd(li[x1][y1], li[x2][y2]) > 1:
            flag = False
            vis[x2][y2] = 1 # lock
            stack.append((x2, y2))
            cnt += 1

    if flag:
        stack.pop(-1)

# 不包含初始空格
print(cnt + 1)


