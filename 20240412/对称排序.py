n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
d = sorted(a, reverse=True)
flag = True
for i in range(n):
    if a[i] != b[i] and a[i] != d[i]:
        flag = False
        break
if flag: print('YES')
else: print('NO')