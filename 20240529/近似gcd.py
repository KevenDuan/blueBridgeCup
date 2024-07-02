n, g = map(int, input().split())
a = [0] + list(map(int, input().split()))
bad, ans, l = 0, 0, 1
for r in range(1, n + 1):
    if a[r] % g != 0:
        l = bad + 1
        bad = r
    ans += r - l
print(ans)