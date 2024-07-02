import os
import sys

class Node:
    def __init__(self, val=0, lm=0, rm=0):
        self.val = val
        self.lm = lm
        self.rm = rm
def pushup(rt):
    tree[rt].val = tree[rt*2].val + tree[rt*2+1].val
    tree[rt].lm = max(tree[rt*2].lm, tree[rt*2].val + tree[rt*2+1].lm)
    tree[rt].rm = max(tree[rt*2+1].rm, tree[rt*2+1].val + tree[rt*2].rm)
def build(l, r, rt):
    if l == r:
        tree[rt].val = a[l]
        if a[l] > 0:
            tree[rt].lm = tree[rt].rm = a[l]
        return
    m = (l + r) // 2
    build(l, m, rt*2)
    build(m+1, r, rt*2+1)
    pushup(rt)
def query(L, R, l, r, rt):
    if R < L:
        return Node()
    if L <= l and R >= r:
        return tree[rt]
    m = (l + r) // 2
    n1, n2 = Node(), Node()
    if L <= m:
        n1 = query(L, R, l, m, rt*2)
    if R >= m+1:
        n2 = query(L, R, m+1, r, rt*2+1)
    return Node(
        n1.val + n2.val,
        max(n1.lm, n1.val + n2.lm),
        max(n2.rm, n2.val + n1.rm))
n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
s = [0] * (n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i]
tree = [Node() for _ in range(4*(n+1))]
build(1, n, 1)
for _ in range(q):
    a, b, c, d = map(int, input().split())
    s1 = query(a, b-1, 1, n, 1).rm
    s2 = query(c+1, d, 1, n, 1).lm
    print(s1 + s2 + s[c] - s[b-1])