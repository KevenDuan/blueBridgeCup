n =int(input())
N = 100010
a = list(map(int, input().split()))
d = {}
i, ans = 0, 0
for j in range(n):
    if a[j] not in d:
        d[a[j]] = j
    else:
        if d[a[j]] < i:
            d[a[j]] = j
        else:
            i = d[a[j]] + 1
            d[a[j]] = j
    ans = max(ans, j - i + 1)
    # print(i, j)
print(ans)
