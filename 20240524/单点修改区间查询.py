def lowbit(x):
    return x & (-x)

def update(x, d):
    while x <= n:
        tree[x] += d
        x += lowbit(x)

def query(x):
    res = 0
    while x:
        res += tree[x]
        x -= lowbit(x)
    return res

n = int(input())
a = [0] + list(map(int, input().split()))
tree = [0] * (n + 1)
for i in range(1, n + 1):
    update(i, a[i])

m = int(input())
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 2:
        print(query(b) - query(a - 1))
    else:
        update(a, b)