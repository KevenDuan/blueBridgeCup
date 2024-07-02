n, m =  map(int, input().split())
li = list(map(int, input().split()))
v = list(map(int, input().split()))

def bin_search(li, value):
    L, R = -1, len(li)
    while L + 1 != R:
        mid = (L + R) // 2
        if li[mid] >= value:
            R = mid
        else: L = mid
    if li[R] == value:
        return R + 1
    else: return -1
    
"""
def bin_search(li, value):
    L, R = 0, len(li)-1
    while L < R:
        mid = (L + R) // 2
        if li[mid] >= value:
            R = mid
        else: L = mid + 1
    if li[R] == value:
        return L + 1
    else: return -1
"""

for i in v:
    print(bin_search(li, i), end = ' ')

