for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    v = a[k-1]
    first_max_idx = None
    for i in range(n): # find first max value
        if a[i] >= v:
            first_max_idx = i
            break
    
    if first_max_idx != None:
        if first_max_idx > k-1: # dont change
            ans = 0
            for i in range(k, n):
                if a[i] <= a[k-1]: ans += 1
                else: break
            if k-1 == 0: print(ans)
            else: print(ans + 1)
        else: # need change
            a[0], a[k-1] = a[k-1], a[0]
            ans1 = 0
            # print(a)
            for i in range(1, n):
                if a[i] < a[0]: ans1 += 1
                else: break
            a[0], a[k-1] = a[k-1], a[0]
            
            a[k-1], a[first_max_idx] = a[first_max_idx], a[k-1]
            # print(a)
            ans2 = 0
            for i in range(first_max_idx+1, n):
                if a[i] <= a[first_max_idx]: ans2 += 1
                else: break
            if first_max_idx == 0: print(max(ans1, ans2))
            else: print(max(ans1, ans2 + 1)) 
    else: # win all competion
        print(n-1)