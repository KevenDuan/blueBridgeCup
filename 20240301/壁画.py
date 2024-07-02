t = int(input())
for d in range(t):
    n = int(input())
    a = [0] + list(map(int, input()))
    prex = [0] * (n + 1)
    for i in range(1, n + 1):
        prex[i] = a[i] + prex[i - 1]

    if n&1: r = n//2 + 1
    else: r = n//2
    res = 0
    for i in range(1, n - r + 2):
        res = max(prex[i + r - 1] - prex[i - 1], res)
    print(f'case #{d+1}: {res}')