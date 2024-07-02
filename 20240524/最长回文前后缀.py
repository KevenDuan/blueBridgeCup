s = list(input())
before = []
after = []
for i in range(1, len(s) + 1):
    before.append(s[:i])
for i in range(1, len(s) + 1):
    after.append(s[len(s) - i:len(s)])

ans = 0
for i in range(len(before)):
    for j in range(len(after)):
        new = before[i] + after[j]
        if new == new[::-1]:
            ans = max(ans, len(new))
print(ans)