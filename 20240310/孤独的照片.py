n = int(input())
N = 5 * 10**5 + 10
a = list(input())
l = [0] * N; r = [0] * N
sh, sg = 0, 0
for i in range(n):
    if a[i] == 'G':
        l[i] = sh
        sh = 0; sg += 1
    else:
        l[i] = sg
        sg = 0; sh += 1
sh, sg = 0, 0
for i in range(n-1, -1, -1):
    if a[i] == 'G':
        r[i] = sh
        sh = 0; sg += 1
    else:
        r[i] = sg
        sg = 0; sh += 1
ans = 0
for i in range(n):
    ans += max(0, l[i]-1) + max(0, r[i]-1) + r[i] * l[i]
print(ans)
    
