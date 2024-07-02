n = int(input())
a = input()
b = input()
c = input()
d = input()
cnt = []
ans = [0] * len(a)
for i in range(n):
    if c[i] < a[i]:
        ans[i] = d[i]
    elif c[i] == a[i]: cnt.append(i)

for i in cnt:
    if d[i] < b[i]:
        ans[i] = d[i]
    else: ans[i] = b[i]

for i in range(len(a)):
    if ans[i] == 0: ans[i] = b[i]
print(''.join(ans))
