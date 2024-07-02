N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))

def search_right(x, li):
    l, r = -1, N-1
    while l + 1 != r:
        mid = (l + r) // 2
        if li[mid] <= x: l = mid
        else: r = mid
    if li[r] > x: return r
    else: return N

def search_left(x, li):
    l, r = 0, N
    while l + 1 != r:
        mid = (l + r) // 2
        if li[mid] < x: l = mid
        else: r = mid
    if li[l] < x: return l
    else: return -1
    
ans = 0
for i in range(N):
    ans += (N - search_right(B[i], C)) * (search_left(B[i], A) + 1)
print(ans)