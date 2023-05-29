n, m, x = map(int, input().split())
a = [0] + list(input().split())
op = [0] * (n+10)
mp = {}
op[n+1] = 1<<30
for i in range(n, 0, -1):
    a[i] = int(a[i])
    mp[a[i]] = i
    op[i] = op[i+1]
    y = x^a[i]
    if mp.get(y): op[i] = min(op[i], mp[y])
for i in range(m):
    l, r = map(int, input().split())
    if op[l] <= r: print('yes')
    else: print('no')
