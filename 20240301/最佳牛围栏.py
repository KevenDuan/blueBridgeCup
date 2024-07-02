import sys
input = sys.stdin.readline
N, F = map(int, input().split())
a = [0]
for i in range(N):
    a.append(int(input()))

def check(ans):
    prex = [0] * (N + 1)
    for i in range(1, N + 1):
        prex[i] = prex[i - 1] + (a[i] - ans)
    minv = 2000
    l, r = 0, F
    while r <= N:
        minv = min(minv, prex[l])
        if prex[r] - minv >= 0: return True
        l += 1; r += 1
    return False

l, r = 0, 2001
while r - l > 1e-5:
    mid = (l + r) / 2
    if check(mid): l = mid
    else: r = mid

print(int(r * 1000))