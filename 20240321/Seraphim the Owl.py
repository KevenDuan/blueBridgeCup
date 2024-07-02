for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    b = list(map(int, input().split()))[::-1]
    prex = [0]
    for i in range(n):
        prex.append(prex[-1] + min(a[i], b[i]))
    mmin = prex[n-m] + a[n-m]
    for i in range(n-m+1, n+1):
        mmin = min(mmin, prex[i-1] + a[i-1])
    print(mmin)
