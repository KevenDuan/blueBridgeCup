n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
tree = [0] * (n + 5)

def lowbit(x):
    return x & (-x)

def update(x, d):
    while x <= n:
        tree[x] += d
        x += lowbit(x)

def query(x):
    ans = 0
    while x:
        ans += tree[x]
        x -= lowbit(x)
    return ans

def update_range(l, r, x):
    for i in range(l, r + 1):
        update(i, x)
        
for i in range(1, n + 1):
    update(i, a[i])

for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        l, r, x = op[1:]
        update_range(l, r, x)
    else:
        l, r = op[1:]
        print(query(r) - query(l - 1))