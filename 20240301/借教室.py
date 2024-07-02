import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [[]]
for _ in range(m):
    b.append(list(map(int, input().split())))

def check(mid):
    diff = [0] * (n + 5)
    for i in range(1, mid + 1): 
        d, s, t = b[i]
        diff[s] += d; diff[t + 1] -= d
    res = 0
    for i in range(1, n + 1):
        res += diff[i]
        if res > a[i]:
            return False
    return True

l, r = 0, m
while l + 1 != r:
    mid = (l + r) // 2
    if check(mid): l = mid
    else: r = mid

if r < m:
    print(-1)
    print(r)
else:
    if check(r): print(0)
    else:
        print(-1)
        print(r)