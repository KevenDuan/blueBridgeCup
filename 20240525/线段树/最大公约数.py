import sys
sys.setrecursionlimit(300000)
from math import gcd
n = int(input())
a = [0] + list(map(int, input().split()))
tree = [0] * ((n << 2) + 10)
def push_up(p):                                     
    tree[p] = gcd(tree[p << 1], tree[p << 1 | 1])   #父节点存储两个子节点的gcd

def build(p, pl, pr):
    if pl == pr:
        tree[p] = a[pl]
        return 
    mid = pl + pr >> 1
    build(p << 1, pl, mid)
    build(p << 1 | 1, mid + 1, pr)
    push_up(p)

def query(p, pl, pr, L, R):
    if L <= pl and pr <= R: return tree[p]
    mid = pl + pr >> 1
    if L > mid:                                     #上面的两种情况，只需要查一个子区间，那就直接返回对应部分结果
        return query(p << 1 | 1, mid + 1, pr, L, R)
    elif R <= mid:
        return query(p << 1, pl, mid, L, R)         #下边两个子区间都要查询，取它们的gcd作为查询结果
    else: return gcd(query(p << 1, pl, mid, L, R), query(p << 1 | 1, mid + 1, pr, L, R))


build(1, 1, n)
if 1 in a:                                  #如果a中有1，那么非1元素个数就是最少的变成全1的操作次数
    print(n - a.count(1))
    sys.exit(0)
if query(1, 1, n, 1, n) != 1:               #如果整个a中所有数的gcd还是非1，那么a必然不能被改成全1
    print(-1)
    sys.exit(0)

ans = int(1e9) + 10
l = 1
for r in range(1, n + 1):
    while query(1, 1, n, l, r) == 1:
        ans = min(ans, r - l)
        l += 1
print(ans + n - 1)