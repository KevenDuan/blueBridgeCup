for _ in range(int(input())):
    a, b, c = map(int, input().split())
    cnta, cntb = map(int, input().split())
    va, vb = map(int, input().split())
    v = [0] + [va] * cnta + [vb] * cntb
    n = cnta + cntb

    dp = [[[[0] * (n + 1) for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]
    ans = 0 
    for i in range(1, n + 1):
        for x in range(a + 1):
            for y in range(b + 1):
                for z in range(c + 1):
                    if x >= v[i]:
                        dp[x][y][z][i] = max(dp[x][y][z][i], dp[x - v[i]][y][z][i - 1] + 1)
                    if y >= v[i]:
                        dp[x][y][z][i] = max(dp[x][y][z][i], dp[x][y - v[i]][z][i - 1] + 1)
                    if z >= v[i]:
                        dp[x][y][z][i] = max(dp[x][y][z][i], dp[x][y][z - v[i]][i - 1] + 1)
                    ans = max(ans, dp[x][y][z][i])

    print(ans)