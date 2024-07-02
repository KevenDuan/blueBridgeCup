n = 10000
mod = 10**9 + 7
ans = (n * (n - 1)) % mod * pow(9, n-2, mod)
print(ans % mod)