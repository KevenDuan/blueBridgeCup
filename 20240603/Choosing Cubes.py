for _ in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] + sorted(a, reverse = True) + [0]
    a = [0] + a
    flag = True
    if b[k + 1] == b[k] == a[f]:
        print('MAYBE')
    else:
        for i in range(1, k + 1):
            if b[i] == a[f]:
                flag = False
        if flag: print('NO')
        else: print('YES')