n = int(input())
N = 33000
tree = [0] * (N)
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
d = {}
for _ in range(n):
    x, y = map(int, input().split())
    x, y = x + 1, y + 1
    tmp = query(x)
    update(x, 1)
    if tmp not in d:
        d[tmp] = 1
    else: d[tmp] += 1

for i in range(n):
    if i not in d: print(0)
    else: print(d[i])
        
