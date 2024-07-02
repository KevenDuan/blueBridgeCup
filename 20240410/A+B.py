def get_prime(N):
    flag = [0] * N
    for i in range(2, N):
        if flag[i] == 0:
            for j in range(i+i, N, i):
                flag[j] = 1
    return flag

N = 1010
flag = get_prime(N)
n = int(input())
dp = [0] * N
dp[0] = 1
for i in range(2, n+1):
    if not flag[i]:
        for j in range(i, n+1):
            dp[j] += dp[j-i]
print(dp[n])