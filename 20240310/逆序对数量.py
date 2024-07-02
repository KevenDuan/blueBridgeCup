from bisect import bisect_left
n = int(input())
N = 10**6 + 10
a = list(map(int, input().split()))
def discrerize(a):
    b = sorted(set(a))
    for i in range(len(a)):
        a[i] = bisect_left(b, a[i]) + 1
    return a
a = discrerize(a)

tree = [0] * N
def lowbit(x): return x & (-x)

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

res = 0
for i in range(n):
    res += i - query(a[i])
    update(a[i], 1)
print(res)
