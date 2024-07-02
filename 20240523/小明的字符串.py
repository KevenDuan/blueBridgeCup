import sys
s = [0] + list(input())
t = [0] + list(input())
n1, n2 = len(s) - 1, len(t) - 1
seed = 121
mod = 10**9 + 7

def hash(s):
    h = [0] * len(s)
    for i in range(1, len(s)):
        h[i] = (h[i - 1] * seed + ord(s[i])) % mod
    return h

def query(h, l, r):
    return (h[r] - h[l-1] * pow(seed, r - l + 1, mod)) % mod

h1, h2 = hash(s), hash(t)
for i in range(n2, 1, -1):
    tmp = query(h2, 1, i)
    for j in range(1, n1 - i + 2):
        if query(h1, j, j + i - 1) == tmp:
            print(i)
            sys.exit()
            