n, m = map(int, input().split())
N = 40
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = [0, 0, 0, 0, 0]
for i in c: b[i] += 1
dp = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
for A in range(b[1]+1):
    for B in range(b[2]+1):
        for C in range(b[3]+1):
            for D in range(b[4]+1):
                t = a[A+B*2+C*3+D*4]
                dp[A][B][C][D] = t
                if A: dp[A][B][C][D] = max(dp[A][B][C][D], dp[A-1][B][C][D] + t)
                if B: dp[A][B][C][D] = max(dp[A][B][C][D], dp[A][B-1][C][D] + t)
                if C: dp[A][B][C][D] = max(dp[A][B][C][D], dp[A][B][C-1][D] + t)
                if D: dp[A][B][C][D] = max(dp[A][B][C][D], dp[A][B][C][D-1] + t)
print(dp[b[1]][b[2]][b[3]][b[4]])
