from bisect import bisect_left
# int(input())
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[::-1]
    prex1 = [0]
    for _ in range(n): # 前缀和
        prex1.append(prex1[-1] + a[_])
    # print(prex1)
        
    prex2 = [0]
    for _ in range(n): # 后缀和
        prex2.append(prex2[-1] + b[_])
    # print(prex2)

    l_cnt = (k + 1)//2
    r_cnt = k//2
    # print(l_cnt, r_cnt)

    l_idx = bisect_left(prex1, l_cnt)
    r_idx = bisect_left(prex2, r_cnt)

    # print(l_idx, r_idx)
    ans = 0
    try:
        if prex1[l_idx] > l_cnt:
            ans += l_idx - 1
        else: ans += l_idx

        if prex2[r_idx] > r_cnt:
            ans += r_idx - 1
        else: ans += r_idx
        
        if k < prex1[-1]:
            print(min(ans, n))
        else: print(n)
    except: print(n)