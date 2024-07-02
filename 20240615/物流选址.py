for _ in range(int(input())):
    p, q = map(int, input().split())
    if p == q:
        print(0)
        continue
    
    ans = 0x3f3f3f3f
    for i in range(1, int((q - p)**0.5) + 1):
        if (q - p) % i == 0:
            if i - p >= 0:
                ans = min(ans, i - p)
            elif (q - p) // i - p >= 0:
                ans = min(ans, (q - p) // i - p)
            
    if ans > 1e9: print(-1)
    else: print(ans)
            