n, q = map(int, input().split())
arr = list(map(int, input().split()))


def s_l(n):
    l, r = -1, len(arr)
    while l + 1 != r:
        m = (l + r) // 2
        if arr[m] < n: l = m
        else: r = m
    return r

def s_r(n):
    l, r = -1, len(arr)
    while l + 1 != r:
        m = (l + r) // 2
        if arr[m] > n: r = m
        else: l = m
    return l

for i in range(q):
    idx = int(input())
    a, b = s_l(idx), s_r(idx)
    if a == len(arr):
        print(-1, -1)
    elif arr[a] != arr[b]:
        print(-1, -1)
    else:
        print(a, b)

