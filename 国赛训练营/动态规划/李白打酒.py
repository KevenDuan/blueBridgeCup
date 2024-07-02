mod = 1000000007
n, m = map(int, input().split())
N = 110
# 遇店x次，遇到花y次，酒壶里还有z斗酒的方案数
dp = [[[0] * N for _ in range(N)] for __ in range(N)]
dp[0][0][2] = 1
for x in range(N-5):
    for y in range(N-5):
        for z in range(N-5):
            # 从遇花状态转移过来
            dp[x][y][z] = (dp[x][y][z] + dp[x][y-1][z+1]) % mod
            # 从遇店状态转移过来
            if z % 2 == 0 and z != 0:
                dp[x][y][z] = (dp[x][y][z] + dp[x-1][y][z//2]) % mod

print(dp[n][m][0] % mod)
            