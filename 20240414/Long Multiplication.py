for _ in range(int(input())):
    x = list(input())
    y = list(input())
    if x[0] < y[0]: x, y = y, x
    n = len(x)
    flag = False
    for i in range(n):
        if (x[i] > y[i]) == flag: x[i], y[i] = y[i], x[i]
        flag |= (x[i] != y[i])
    print(''.join(x))
    print(''.join(y))
