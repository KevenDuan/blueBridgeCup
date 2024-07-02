import sys
sys.setrecursionlimit(10**5)
w = int(input())
h = int(input())
Map = [list(input()) for _ in range(h)]
vis = [[0] * (w+1) for _ in range(h+1)]
d = {}
def distance(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

def dfs(x, y, tag, no):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            xn, yn = x + i, y + j
            if xn < 0 or xn >= h or yn < 0 or yn >= w: continue
            if vis[xn][yn] == no or Map[xn][yn] == '0': continue
            Map[xn][yn] = tag
            vis[xn][yn] = no
            dfs(xn, yn, tag, no)
            top.append([xn, yn])

def taging(top, t):
    global cnt
    res = 0
    for i in range(len(top)):
        for j in range(len(top)):
            res += distance(top[i], top[j])
    res = int(res)
    if res not in d:
        d[res] = t
        cnt += 1
        dfs(top[0][0], top[0][1], t, 2)
    else:
        dfs(top[0][0], top[0][1], d[res], 2)
    
cnt = 0
for i in range(h):
    for j in range(w):
        if vis[i][j] == 0 and Map[i][j] == '1':
            top = [[i,j]]
            vis[i][j] = 1
            dfs(i, j, '1', 1)
            if len(top) != 0:
                taging(top, chr(ord('a')+cnt))

for i in range(h):
    print(''.join(Map[i]))
            
    
