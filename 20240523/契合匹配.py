n = int(input())
a = list(input())
b = list(input())
p = 233
mod = 10**9 + 7

def turn(s): # 大小写转换
    for i in range(n):
        if ord('A') <= ord(s[i]) <= ord('Z'):
            s[i] = chr(ord(s[i]) + 32)
        else: s[i] = chr(ord(s[i]) - 32)
    return s

def hash(s):
    n = len(s)
    h = [0] * n
    for i in range(1, n):
        h[i] = (h[i - 1] * p + ord(s[i])) % mod
    return h
        
def query(h, l, r):
    return (h[r] - h[l-1] * pow(p, r - l + 1, mod)) % mod

a = [0] + turn(a) * 2
b = [0] + b
h1, h2 = hash(a), hash(b)
ans = 0x3f3f3f3f

for i in range(1, n + 2):
    if h2[-1] == query(h1, i, i + n - 1):
        ans = min(ans, i - 1, n - i + 1)

if ans > 1e9:
    print('No')
else:
    print(f'Yes\n{ans}')