import sys
input = sys.stdin.readline
n = int(input())
mod = 998244353
cnt = n-2
A = n
res = 1
while cnt:
    res = (res * A) % mod
    A -= 1
    cnt -= 1
res = res % mod
ans = res * (n-1) + (n-1)*(n-2)*res//2
print(ans%mod)
