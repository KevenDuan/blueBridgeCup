n, k = map(int, input().split())
a = list(map(int, input().split()))
dp1 = [1] * n
for i in range(1, n):
    if a[i] >= a[i-1]:
        dp1[i] += dp1[i-1]

dp2 = [1] * n
for i in range(n-2, -1, -1):
    if a[i] <= a[i+1]:
        dp2[i] += dp2[i+1]

a = [0] + a + [0]
dp1 = [0] + dp1 + [0]
dp2 = [0] + dp2 + [0]
def check(x):
    j = k; mm = 0
    for i in range(1, n-k+2):
        print(i, j, mm)
        if a[i-1] <= a[j+1]:
            mm = max(mm, k + dp1[i-1] + dp2[j+1])
        else:
            mm = max(mm, k + dp1[i-1], k + dp2[j+1])
        j += 1
    if mm >= x: return True
    else: return False

l, r = 0, 10**6+10
while l + 1 != r:
    mid = (l + r) // 2
    if check(mid): l = mid
    else: r = mid
print(l)
