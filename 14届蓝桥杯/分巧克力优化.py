def check(d):
    res = 0
    for i in range(n):
        res += (h[i]//d) * (w[i]//d)
    if res >= k: return True
    else: return False
    
n, k = map(int, input().split())
h = [0] * 100100
w = [0] * 100100
for i in range(n):
    h[i], w[i] = map(int, input().split())

left = 1
right = 100100
while left < right:
    mid = (left + right) // 2
    # print(left, mid, right)
    if check(mid): left = mid + 1
    else: right = mid

print(left - 1)
