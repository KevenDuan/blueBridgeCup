for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    vis = [0] * (n+1)
    p = []; Mex = 0
    if a[0] == 1: # choose zero
        p.append(0)
        vis[0] = 1
        Mex = 1
    else: # choose other
        p.append(-a[0])
        vis[-a[0]] = 1 # Mex = 0

    def update(x):
        for i in range(x, n):
            if vis[i] == 0:
                return i
            
    for i in range(1, n):
        # if p(i) can update Mex
        if a[i] == 1:
            p.append(Mex)
            vis[Mex] = 1
            Mex = update(Mex)
        elif Mex - a[i] < 0 or vis[Mex-a[i]] == 1:
            tmp = update(0)
            p.append(tmp)
            vis[tmp] = 1
            Mex = update(Mex)
        else: # cant update
            p.append(Mex - a[i])
            vis[Mex-a[i]] = 1
            Mex = update(Mex)
            
    print(*p)
    
    
        
