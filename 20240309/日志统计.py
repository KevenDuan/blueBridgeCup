n, d, k = map(int, input().split())
N = 10**5 + 10
a = []
for _ in range(n): a.append(list(map(int, input().split())))
a.sort()

st = [False] * N
cnt = [0] * N
j = 0
for i in range(n):
    cnt[a[i][1]] += 1 # cnt[id]++
    while a[i][0] - a[j][0] >= d:
        cnt[a[j][1]] -= 1
        j += 1
    if cnt[a[i][1]] >= k: st[a[i][1]] = True

for i in range(N):
    if st[i]: print(i)
