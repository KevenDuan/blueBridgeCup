def build(p, pl, pr):
    if pl == pr:
        tree[p] = -INF
        return
    mid = (pl + pr)>>1
    build(p<<1, pl, mid)
    build(p<<1|1, mid+1, pr)
    tree[p] = max(tree[p<<1], tree[p<<1|1])

def update(p, pl, pr, l, r, d):
    if l <= pl and pr <= r:
        tree[p] = d
        return
    mid = (pl + pr)>>1
    if l <= mid: update(p<<1, pl, mid, l, r, d)
    if r > mid: update(p<<1|1, mid+1, pr, l, r, d)
    tree[p] = max(tree[p<<1], tree[p<<1|1]) # push_up
    return

def query(p, pl, pr, l, r):
    res = -INF
    if l <= pl and pr <= r:
        return tree[p]
    mid = (pl + pr)>>1
    if l <= mid: res = max(res, query(p<<1, pl, mid, l, r))
    if r > mid: res = max(res, query(p<<1|1, mid+1, pr, l, r))
    return res


N = 100001
tree = [0] * (N<<2)
INF = 0X7FFFFFFF
M, D = map(int, input().split())
cnt = 0
t = 0
build(1, 1, N) # 建立线段树
for i in range(M):
    op = list(input().split())
    if op[0] == 'A':
        cnt += 1
        update(1, 1, N, cnt, cnt, (int(op[1])+t)%D)
    if op[0] == 'Q':
        t = query(1, 1, N, cnt-int(op[1])+1, cnt)
        print(t)
