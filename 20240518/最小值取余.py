n = int(input())
a = sorted(map(int, input().split()))
mod = 998244353
x = 0

def func(x, i):
    return x * 10 + a[i]

for i in range(n):
    x = func(x, i) % mod
    
print(x % mod)