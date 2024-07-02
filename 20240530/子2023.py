s = ''
for i in range(1, 2023 + 1):
    s += str(i)

dp = [0, 0, 0, 0] # '2' '20' '202' '2023'
for i in s:
    if i == '2':
        dp[0] += 1
        dp[2] += dp[1]
    elif i == '0':
        dp[1] += dp[0]
    elif i == '3':
        dp[3] += dp[2]
print(dp[3])
        