t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split())) + [0, 0]
    b = [0] * (n + 2)
    for i in range(n):
        if b[i] > a[i]: break
        d = a[i] - b[i]
        b[i] += d; b[i+2] += d
        b[i+1] += d * 2
    if b == a: print('YES')
    else: print('NO')
