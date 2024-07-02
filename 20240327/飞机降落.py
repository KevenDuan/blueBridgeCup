for _ in range(int(input())):
    n = int(input())
    N = 11
    T = []; D = []; L = [];
    for _ in range(n):
        t,d,l = map(int, input().split())
        T.append(t)
        D.append(d)
        L.append(l)

    dp = [[0x3f3f3f3f] * (N) for _ in range(1<<N)]
    for i in range(n):
        dp[1<<i][i] = T[i]+L[i]

    for i in range(1<<N):
        for j in range(n):
            if i >> j & 1:
                for k in range(n):
                    if (i-(1<<j)) >> k & 1: # 保证了j和k在i中
                        if T[j] >= dp[i-(1<<j)][k]:
                            dp[i][j] = min(dp[i][j], T[j] + L[j])
                        elif T[j] + D[j] >= dp[i-(1<<j)][k]:
                            dp[i][j] = min(dp[i][j], dp[i-(1<<j)][k] + L[j])

    if min(dp[(1<<n)-1]) != 0x3f3f3f3f:
        print('YES')
    else: print('NO')
