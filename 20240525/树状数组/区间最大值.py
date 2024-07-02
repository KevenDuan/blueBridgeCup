import sys
sys.setrecursionlimit(10**5)
def bulid(id, l, r):
    if l == r:
        tree[id] = a[l]
        return
    mid = (l + r) // 2
    bulid(id * 2, l, mid)
    bulid(id * 2 + 1, mid + 1, r)
    tree[id] = max(tree[id * 2], tree[id * 2 + 1])
    
def query(L, R, id, l, r):
    if R < l or L > r: return -0x3f3f3f3f
    if L <= l and r <= R: return tree[id]
    mid = (l + r) // 2
    return max(query(L, R, id * 2, l, mid), query(L, R, id * 2 + 1, mid + 1, r))

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
tree = [0] * (n<<2)
bulid(1, 1, n)
for _ in range(q):
    x, y = map(int, input().split())
    print(query(x, y, 1, 1, n))