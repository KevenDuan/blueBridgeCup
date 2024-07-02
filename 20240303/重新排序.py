n = int(input())
a = [0] + list(map(int, input().split()))
q = int(input())
diff = [0] * (n + 2)
s = [0] * (n + 1)
cnt = 0
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
for _ in range(q):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1
    cnt += s[r] - s[l - 1]
b = sorted(a, reverse=True)
prex = [0] * (n + 1)
for i in range(1, n + 1):
    prex[i] = prex[i - 1] + diff[i]
prex.sort(reverse=True)
ans = 0
for i in range(n + 1):
    if prex[i] == 0: break
    ans += prex[i] * b[i]
print(ans - cnt)