for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == k:
        print(*[1] * n)
    elif k == 1:
        print(*[i for i in range(1, n+1)])
    else:
        print(-1)
