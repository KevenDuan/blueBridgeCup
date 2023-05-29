def binsearch(li, v):
    l = 0
    r = len(li)
    while l < r:
        mid = (l + r) // 2
        print(mid)
        if li[mid] >= v: r = mid
        else: l = mid + 1
        print(l, r)


li = [1, 2, 2, 3, 4, 5]
binsearch(li, 2)
