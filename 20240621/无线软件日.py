n = int(input())
s = input().lower()
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else: d[i] += 1
tmp = 'shanghai'
ans = 0x3f3f3f3f
for i in tmp:
    if i == 'h' or i == 'a':
        ans = min(ans, d[i] // 2)
    else: ans = min(ans, d[i])
print(ans)