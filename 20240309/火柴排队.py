from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
N = 10**5 + 10
mod = 99999997
def discretize(li):
    t = list(set(sorted(li)))
    for i in range(len(li)):
        li[i] = bisect_left(t, li[i]) + 1
    return li
a = discretize(a)
b = discretize(b)
for i in range(n): a[i] = [a[i], i + 1]
for i in range(n): b[i] = [b[i], i + 1]
a.sort(); b.sort()
p = [0] * (n + 1)
for i in range(n):
    p[a[i][1]] = b[i][1]
def lowbit(x): return x & (-x)
tree = [0] * N
def update(x, d):
    while x <= N:
        tree[x] += d
        x += lowbit(x)
def query(x):
    ans = 0
    while x:
        ans += tree[x]
        x -= lowbit(x)
    return ans
ans = 0
for i in range(1, n + 1):
    ans += (i - query(p[i]) - 1) % mod
    update(p[i], 1)
print(ans % mod)
