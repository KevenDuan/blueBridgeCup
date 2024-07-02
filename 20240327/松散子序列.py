s = list(input())
s = [0] + [ord(i)-ord('a')+1 for i in s]
n = len(s)
dp = [0] * (n+1)
dp[1] = s[1]
for i in range(2, n):
    dp[i] = max(dp[i-2] + s[i], dp[i-1])
print(dp[n-1])
