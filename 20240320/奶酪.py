for _ in range(int(input())):
    n, h, r = map(int, input().split())
    axis = [list(map(int, input().split())) for _ in range(n)]
    vis = [0] * (n + 1)
    p = [i for i in range(n+1)]

    def distance(x1, y1, z1, x2, y2, z2):
        return ( (x1-x2)**2 + (y1-y2)**2 + (z1 - z2)**2 )**0.5

    def find(x):
        if x == p[x]:
            return x
        p[x] = find(p[x])
        return p[x]
    
    def merge(x, y):
        xRoot = find(x)
        yRoot = find(y)
        p[xRoot] = yRoot

    def query(x, y):
        return find(x) == find(y)

    for i in range(n):
        x1, y1, z1 = axis[i]
        for j in range(i+1, n):
            x2, y2, z2 = axis[j]
            if distance(x1, y1, z1, x2, y2, z2) <= 2 * r:
                merge(i, j)

    flag = False
    for i in range(n):
        x1, y1, z1 = axis[i]
        if flag: break
        if z1 - r > 0: continue
        for j in range(n):
            x2, y2, z2 = axis[j]
            if z2 + r >= h:
                if query(i, j):
                    flag = True
                    break
    if flag: print('Yes')
    else: print('No')
