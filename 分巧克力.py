n, k = map(int, input().split())
h = [0]
w = [0]
for i in range(n):
    a, b = map(int, input().split())
    h.append(a)
    w.append(b)

def binary():
    l, r = -1, 100100
    while l + 1 != r:
        mid = (l + r) // 2
        if not judge(mid): # 巧克力切大了
            r = mid
        else: l = mid # 巧克力切小了
    return mid
            
def judge(mmax):
    final = 0 # 已经分到巧克力的小朋友
    for i in range(1, n + 1): # 遍历小明所有的巧克力
        if h[i] * w[i] < mmax * mmax: # 面积过小的巧克力不能被切分
            continue
        if h[i] >= mmax and w[i] >= mmax: # 长宽至少够切一个的巧克力
            t_h = h[i] // mmax
            t_w = w[i] // mmax
            final += t_h * t_w
    if final < k: return False # 不够分
    else: return True # 够分

ans = binary()
for i in range(ans + 3, ans - 3, -1):
    if judge(i):
        print(i)
        break
    
