n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + sorted(arr)
cnt = 0
for i in range(1, n + 1):
    lt = l - arr[i]
    rt = r - arr[i]
    
    L1, R1 = i, n + 1
    while L1 + 1 != R1:
        mid = (L1 + R1) // 2
        if arr[mid] > rt: R1 = mid
        else: L1 = mid
    L2, R2 = i, n + 1
    while L2 + 1 != R2:
        mid = (L2 + R2) // 2
        if arr[mid] < lt: L2 = mid
        else: R2 = mid
    ans = L1 - R2 + 1
    if ans > 0: cnt += ans
print(cnt)
        
    

        