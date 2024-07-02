import sys
n = int(input())
N = int(n**0.5) + 1
d = {}
for i in range(N):
    for j in range(N):
        s = i*i + j*j
        if s > n: continue
        if s not in d: d[s] = i

for i in range(N):
    for j in range(N):
        s = i*i + j*j
        if s > n: continue
        t = n - s
        if t not in d: continue
        c = int((t - d[t]*d[t])**0.5)
        l = [d[t], i, j, c]
        l.sort()
        print(*l)
        sys.exit()
            
