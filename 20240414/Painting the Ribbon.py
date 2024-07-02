for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if n <= m and k < n-1: print('YES')
    elif n >= m and (n%m) == 0 and k < (n // m) * (m - 1) + (n % m): print('YES')
    elif n >= m and (n%m) != 0 and k < (n // m) * (m - 1) + (n % m)-1: print('YES')
    else: print('NO')