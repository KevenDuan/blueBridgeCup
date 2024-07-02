for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))
    
    old = {}
    for i in b:
        if i not in old:
            old[i] = 1
        else: old[i] += 1
        
    vis = {}
    for i in d:
        if i not in vis:
            vis[i] = 1
        else: vis[i] += 1

    flag = True
    for i in range(1, n + 1):
        if a[i] == b[i]:
            continue
        
        if b[i] in vis and vis[b[i]] != 0:
            vis[b[i]] -= 1
        else:
            flag = False
            break
    
    if d[-1] not in old:
        flag = False
        
    if flag: print('YES')
    else: print('NO')