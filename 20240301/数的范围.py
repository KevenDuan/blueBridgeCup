def search_left(x):
    l, r = -1, len(a) - 1
    while l + 1 != r:
        mid = (l + r) // 2
        if a[mid] >= x: r = mid
        else: l = mid
    if a[r] != x: return -1
    return r

def search_right(x):
    l, r = 0, len(a)
    while l + 1 != r:
        mid = (l + r) // 2
        if a[mid] <= x: l = mid
        else: r = mid
    if a[l] != x: return -1
    return l

n, q = map(int, input().split())     
a = list(map(int, input().split()))
for _ in range(q):
    b = int(input())
    print(f'{search_left(b)} {search_right(b)}')