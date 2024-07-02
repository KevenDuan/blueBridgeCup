for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else: d[a[i]] += 1
        
    ans = 0
    for k, v in d.items():
        ans += v // 3
    print(ans)