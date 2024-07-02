def build(id, l, r):
    if l == r:
        tree[id] = a[l]
        return
    mid = (l + r) // 2
    build(id * 2, l, mid)
    build(id * 2 + 1, mid + 1, r)
    tree[id] = tree[id * 2] + tree[id * 2 + 1]
    
def to_down(id, sl, sr):
    tag[id * 2] += tag[id]
    tag[id * 2 + 1] += tag[id]
    tree[id * 2] += tag[id] * sl
    tree[id * 2 + 1] += tag[id] * sr
    tag[id] = 0
    
def update(L, R, v, id, l, r):
    if R < l or L > r: return
    if L <= l and r <= R:
        tag[id] += v
        tree[id] += v * (r - l + 1)
        return
    mid = (l + r) // 2
    to_down(id, mid - l + 1, r - mid)
    update(L, R, v, id * 2, l, mid)
    update(L, R, v, id * 2 + 1, mid + 1, r)
    tree[id] = tree[id * 2] + tree[id * 2 + 1]
    
def query(L, R, id, l, r):
    if R < l or L > r: return 0
    if L <= l and r <= R: return tree[id]
    mid = (l + r) // 2
    to_down(id, mid - l + 1, r - mid)
    return query(L, R, id * 2, l, mid) + query(L, R, id * 2 + 1, mid + 1, r)
        
n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
tag = [0] * (n<<2)
tree = [0] * (n << 2)
build(1, 1, n)  # 建树
for i in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        x, y, z = op[1:]
        update(x, y, z, 1, 1, n)
    else:
        x, y = op[1:]
        print(query(x, y, 1, 1, n))