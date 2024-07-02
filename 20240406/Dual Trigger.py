for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input())]
    cnt = 0
    for i in range(n):
        if a[i] == 1: cnt += 1

    if cnt&1:
        print('NO')
    elif cnt == 2:
        flag = False
        for i in range(n-1):
            if a[i] == a[i+1] == 1:
                flag = True
                break
        if flag: print('NO')
        else: print('YES')
    else:
        print('YES')
    