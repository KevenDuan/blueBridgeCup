n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
a.sort()

l, r = a[0][0], a[0][1]
ans1, ans2 = r - l, 0
for i in range(1, n):
    if l <= a[i][0] <= r:
        r = max(r, a[i][1])
    else:
        ans2 = max(ans2, a[i][0] - r)
        l, r = a[i][0], a[i][1]
    ans1 = max(ans1, r - l)
print(ans1, ans2)
