n, m = map(int, input().split())
a = [0] + list(input())
p = 131
mod = 10**9 + 7
h = [0] * (n + 1)
for i in range(1, n + 1):
    h[i] = (h[i-1] * p + ord(a[i])) % mod

def query(l, r):
    return (h[r] - h[l-1] * pow(p, (r-l+1), mod)) % mod

for _ in range(m):
    l1, r1, l2, r2 = map(int, input().split())
    if  query(l1, r1) == query(l2, r2):
        print('Yes')
    else: print('No')
    
