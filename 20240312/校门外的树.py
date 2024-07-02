L, M = map(int, input().split())
a = []
for _ in range(M):
    a.append(list(map(int, input().split())))
a.sort()
a.append([L+1, L+1])

l, r = a[0][0], a[0][1]
for i in range(1, M + 1):
    if l <= a[i][0] <= r: r = max(r, a[i][1])
    elif r < a[i][0]:
        L -= r - l + 1
        l, r = a[i][0], a[i][1]
print(L+1)
