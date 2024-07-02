def hash(s):
    n = len(s)
    h = [0] * n
    for i in range(1, n):
        h[i] = (h[i - 1] * seed + ord(s[i])) % mod
    return h 

def query(h, l, r):
    return (h[r] - h[l - 1] * pow(seed, r - l + 1)) % mod

seed = 233
mod = 10**9 + 7
s = list(input())
s1, s2 = [0] + s, [0] + s[::-1]
h1, h2 = hash(s1), hash(s2)

l, r = 0, len(s) + 1
while l + 1 != r:
    mid = (l + r) // 2
    if query(h1, 1, mid) == query(h2, 1, mid):
        l = mid
    else: r = mid

extra = 0
s3, s4 = [0] + s1[l+1:], [0] + s1[l+1:][::-1]
h3, h4 = hash(s3), hash(s4)
for i in range(1, len(s3)):
    if query(h3, 1, i) == query(h4, len(s3) - i, len(s3) - 1):
        extra = i
print(l * 2 + extra)