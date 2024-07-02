import sys
input = sys.stdin.readline
for ___ in range(int(input())):
# for ___ in range(1):
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    dire = {}
    for _ in range(len(a)):
        if a[_] not in dire: dire[a[_]] = 1
        else: dire[a[_]] += 1

    aii = min(a)

    flag = True
    for __ in range(n):
        if flag == False: break
        arr = [aii]
        for _ in range(n):
            # print(arr[-1])
            if arr[-1] not in dire:
                flag = False
                break
            else: 
                if dire[arr[-1]] == 0:
                    flag = False
                    break
                dire[arr[-1]] -= 1
            if _ != n-1: arr.append(arr[-1] + d)
        # print(arr)
        aii = aii + c

    if flag: print('YES')
    else: print('NO')