n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
a.sort()

l, r = a[0][0], a[0][1]
cnt = 1
for i in range(1, n):
    if  l <= a[i][0] <= r: r = max(r, a[i][1])
    elif r < a[i][0]:
        l, r = a[i][0], a[i][1]
        cnt += 1
print(cnt)
