n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j = 0, 0
for i in range(m):
    if b[i] == a[j]:
        j += 1
    if j == n:
        break
if j == n: print('Yes')
else: print('No')
