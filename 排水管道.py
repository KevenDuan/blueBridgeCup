n = int(input())
h = list(map(int, input().split()))

def Left(h):
    co = h.copy()
    left = 1
    cnt1 = 0
    while left != n:
        if co[left] < co[left-1]:
            pass
        else:
            if co[left-1] == 1:
                cnt1 += Right(co)
                break
            else:
                co[left] = co[left-1] - 1
                cnt1 += 1
        left += 1
        print(co)
    print('-------')
    return cnt1
        
def Right(h):
    cy = h.copy()
    right = n-2
    cnt2 = 0
    while right != -1:
        if cy[right] > cy[right+1]:
            pass
        else:
            cy[right] = cy[right+1] + 1
            cnt2 += 1
        right -= 1
        print(cy)
    return cnt2

a = Left(h)
b = Right(h)
print(min(a, b))
