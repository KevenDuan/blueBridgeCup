for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    tag = a[0]
    ans = 0x3f3f3f3f
    judge = -1
    for i in range(1, n-1):
        if a[i] != tag:
            ans = min(i-judge-1, ans, n-i-1)
            judge = i
    if ans == 0x3f3f3f3f: print(-1)
    else: print(ans)