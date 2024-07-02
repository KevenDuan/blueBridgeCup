s = input()
dp = [1] * len(s)
for i in range(len(s)):
    flag = 0
    for j in range(i, -1, -1):
        if s[j] < s[i]:
            dp[i] += dp[j]
        elif s[j] == s[i] and not flag:
            dp[i] = dp[i] + dp[j] - 1
            flag = 1
print(sum(dp)) # dp[1, 1, 1]
