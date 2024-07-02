for _ in range(int(input())):
    n, m = map(int, input().split())
    flag = False
    if m > 20: m = 20
    for i in range(2, m + 1):
        if n % i != i - 1:
            flag = True
            break
    if flag: print('Yes')
    else: print('No')