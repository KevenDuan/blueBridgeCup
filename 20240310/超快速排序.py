import sys
from bisect import bisect_left
input = sys.stdin.readline
N = 5*10**5 + 10
def discretized(a):
    b = sorted(set(a))
    for i in range(len(a)):
        a[i] = bisect_left(b, a[i]) + 1
    return a

def lowbit(x): return x & (-x)
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

while True:
    tree = [0] * N
    n = int(input())
    if not n: break
    a = []
    for _ in range(n):
        a.append(int(input()))
    a = discretized(a)
    res = 0
    for i in range(n):
        res += i - query(a[i])
        update(a[i], 1)
    print(res)
