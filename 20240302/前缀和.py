n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
prex = [0] * (n + 1)
for i in range(1, n + 1):
    prex[i] = prex[i - 1] + a[i]

for _ in range(m):
    l, r = map(int, input().split())
    print(prex[r] - prex[l - 1])