n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
def check(mid):
    res = 0
    for i in range(n):
        res += (a[i][0] // mid) * (a[i][1] // mid)
    if res >= k: return True
    return False

l, r = 0, 10**5 + 5
while l + 1 != r:
    mid = (l + r) // 2
    if check(mid): l = mid
    else: r = mid
print(l)