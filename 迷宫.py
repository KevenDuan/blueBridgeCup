from collections import deque
q = deque([(0, 0, '')])
dir = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
mp = []
for i in range(30):
    mp.append(list(input()))
mp[0][0] = '1'
# bfs
while q:
    x, y, p = q.popleft()
    # print(x, y, p)
    if x == 29 and y == 49:
        print(p)
        break
    for i in dir:
        nx = x + i[0]
        ny = y + i[1]
        np = p + i[2]
        if nx >= 0 and ny >= 0 and nx <= 29 and ny <= 49 and mp[nx][ny] == '0':
            mp[nx][ny] = '1'
            q.append((nx, ny, np))
