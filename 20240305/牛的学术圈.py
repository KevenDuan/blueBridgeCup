import sys
n, L = map(int, input().split())
c = sorted(map(int, input().split()))
def check(ans):
    res, cnt = 0, 0
    for i in range(n-1, -1, -1):
        cnt += 1
        if c[i] < ans:
            if c[i] + 1 < ans: return False
            res += ans - c[i]
        if cnt == ans: break
    return res <= L

l, r = 0, 10**5 + 1
while l + 1 != r:
    mid = (l + r) // 2
    if check(mid): l = mid
    else: r = mid

print(l)

