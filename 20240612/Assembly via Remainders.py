for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    a = [510]
    for i in range(n - 1):
        a.append(a[-1] + x[i])
    print(*a)