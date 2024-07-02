def build(id, l, r):
    if l == r:
        tree[id] = a[l]
        return
    mid = (l + r) // 2
    build(id * 2, l, mid)
    build(id * 2 + 1, mid + 1, r)
    tree[id] = tree[id * 2] + tree[id * 2 + 1]
    
def update(pos, v, id, l, r):
    if l == r:
        tree[id] += v
        return
    mid = (l + r) // 2
    if pos <= mid: update(pos, v, id * 2, l, mid)
    else: update(pos, v, id * 2 + 1, mid + 1, r)
    tree[id] = tree[id * 2] + tree[id * 2 + 1]

def query(L, R, id, l, r):
    if L > r or R < l: return 0
    if L <= l and r <= R: return tree[id]
    mid = (l + r) // 2
    return query(L, R, id * 2, l, mid) + query(L, R, id * 2 + 1, mid + 1, r)
    
n = int(input())
a = [0] + list(map(int, input().split()))
tree = [0] * (4 * n)
build(1, 1, n)
for _ in range(int(input())):
    op, x, y = map(int, input().split())
    if op == 1:
        update(x, y, 1, 1, n)
    else:
        print(query(x, y, 1, 1, n))
