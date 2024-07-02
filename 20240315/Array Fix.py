t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[n-1]]
    flag1 = True
    for i in range(n-2, -1, -1):
        if a[i] < 10 and a[i] > b[-1]:
            flag1 = False
            break
        if a[i] > b[-1]:
            t1, t2 = a[i]//10, a[i]%10
            if t1 > t2:
                flag1 = False
                break
            elif t2 > b[-1]:
                flag1 = False
                break
            else:
                b.append(t2)
                b.append(t1)
        else: b.append(a[i])
    if flag1: print('YES')
    else: print('NO')
