from math import gcd
a, b = map(int, input().split())
p = int(input())
max_gcd = gcd(a, b)
res = [1]

for i in range(1, int(max_gcd**0.5)+1):
    if max_gcd % i == 0:
        res.append(i)
        res.append(max_gcd//i)
res = sorted(set(res))
    
for _ in range(p):
    l, r = map(int, input().split())
    
    for i in range(len(res)-1, 0, -1):
        if l <= res[i] <= r:
            print(res[i])
            break
    else: print(-1)