s1 = [0] + list(input())
s2 = [0] + list(input())
mod = 10**9 + 7
seed = 121

def get_hash(s):
    n = len(s)
    h = [0] * n
    for i in range(1, n):
        h[i] = (h[i-1] * seed + ord(s[i])) % mod
    return h
        
def query(h, l, r):
    return (h[r] - h[l-1] * pow(seed, r - l + 1, mod)) % mod
        
h1 = get_hash(s1)
h2 = get_hash(s2)
l1, l2 = len(s1)-1, len(s2)
cnt = 0

template = query(h1, 1, l1 - 1)
for i in range(1, l2 - l1 + 1):
    if template == query(h2, i, i + l1 - 2):
        cnt += 1
print(cnt)