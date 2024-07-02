s = list(input())
n = len(s)
ans = 0
for i in range(n):
    l, r = 0, 0
    for j in range(i-1, -1, -1):
        if s[j] != s[i]: l += 1
        else: break
    for j in range(i+1, n, 1):
        if s[j] != s[i]: r += 1
        else: break
    ans += l + r + l * r + 1
print(ans)
