# question1
a = list(map(int, input().split()))
n = len(a)
dp = [1] * (n + 1)
for i in range(n):
    for j in range(0, i):
        if a[j] >= a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# question2
b = [[a[0]]]
for j in range(1, n):
    for i in range(len(b)):
        if b[i][-1] >= a[j]:
            b[i].append(a[j])
            break
    else: b.append([a[j]])
    
print(max(dp))
print(len(b))