n, m, k = map(int, input().split())
narr = [0] + list(map(int, input().split())); dn = [0]
marr = [0] + list(map(int, input().split())); dm = [0]
ln, lm = len(narr), len(marr); mm = max(ln, lm)
for i in range(1, mm):
    if i < ln: dn.append(dn[i - 1] + narr[i])
    if i < lm: dm.append(dm[i - 1] + marr[i])

def getRight(li, num):
    l, r = -1, len(li)
    while l + 1 < r:
        mid = (l + r)//2
        if li[mid] > num: r = mid
        else: l = mid
    return l
        
ans = 0
for i in range(0, n + 1):
    if dn[i] > k: break
    tmp = k - dn[i]
    j = getRight(dm, tmp)
    ans = max(ans, i + j - 1)
print(ans)