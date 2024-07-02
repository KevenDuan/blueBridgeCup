for _ in range(int(input())):
    n, x = map(int, input().split())
    if x >= n/2: print('YES')
    else: print('NO')