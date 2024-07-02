n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check(x):
    num = k
    for i in range(n):
        if b[i] < a[i] * x:
            num -= a[i] * x - b[i]
        if num < 0:
            break
    if num < 0: return False
    else: return True

l, r = 0, 10**18
while l + 1 != r:
    mid = (l + r) // 2
    if check(mid): l = mid
    else: r = mid
print(l)
