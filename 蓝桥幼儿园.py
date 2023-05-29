def link(x, y):
    x = find_set(x)
    y = find_set(y)
    if x != y: f[x] = f[y]

def find_set(x):
    if x != f[x]: f[x] = find_set(f[x])
    return f[x]

n, m = map(int, input().split())
f = [i for i in range(n + 1)]    
for i in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        link(x, y)
    elif op == 2:
        if find_set(x) == find_set(y): print('YES')
        else: print('NO')
