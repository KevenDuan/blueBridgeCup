def find_root(x):
    if x == p[x]: return x
    else:
        p[x] = find_root(p[x])
        return p[x]

def merge(x, y):
    x_root = find_root(x)
    y_root = find_root(y)
    p[x_root] = y_root
    
m, n = map(int, input().split())
p = list(range(m * n + 1))
for _ in range(int(input())):
    u, v = map(int, input().split())
    merge(u, v)

cnt = 0
for i in range(1, m * n + 1):
    root = find_root(i)
    if i == root:
        cnt += 1
print(cnt)