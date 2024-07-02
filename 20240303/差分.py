n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
diff = [0] * (n + 1) + [0]
for i in range(1, n + 1): diff[i] = a[i] - a[i - 1]
for _ in range(m):
    l, r, c = map(int, input().split())
    diff[l] += c
    diff[r + 1] -= c
prex = 0; b = []
for i in range(1, n + 1):
    prex += diff[i]
    b.append(prex)
print(*b)
