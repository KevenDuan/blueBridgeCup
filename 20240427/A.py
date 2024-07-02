for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    b = [0] * 105
    for i in a:
        b[i] += 1

    if n == 1 or max(b) < k:
        print(n)
    else:
        print(k-1)