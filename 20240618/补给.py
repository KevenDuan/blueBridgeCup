n, B = map(int, input().split())
p = [0x3f3f3f3f]
p_new = [0x3f3f3f3f]
for _ in range(n):
    p.append(list(map(int, input().split())))
    
for _ in range(1, n + 1):
    t1, t2 = p[_]
    p_new.append(t1//2 + t2)
    p[_] = sum(p[_])

ans = 0
for i in range(1, n + 1):
    cnt, b = 1, B
    if b - p_new[i] >= 0:
        b -= p_new[i]
    else: continue
    
    p_sort = sorted(p[:i] + p[i+1:])
    j = 0
    while b - p_sort[j] >= 0 and j < n - 1:
        b -= p_sort[j]
        j += 1
        cnt += 1
    ans = max(ans, cnt)

print(ans)