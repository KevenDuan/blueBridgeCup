n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
N = 21; inf = 0x3f3f3f3f
dp = [[inf] * N for _ in range(1<<N)]
dp[1][0] = 0
for i in range(1, 1<<N, 2):
    for j in range(n):
        if i>>j & 1: # 判断状态中是否有目标路
            for k in range(n): # 判断状态是否有中间路
                if (i - (1<<j))>>k & 1:
                    dp[i][j] = min(dp[i][j], dp[i - (1<<j)][k] + Map[k][j])
res = inf
for i in range(1, n):
    res = min(res, dp[(1<<n) - 1][i] + Map[i][0])
print(res)
    
