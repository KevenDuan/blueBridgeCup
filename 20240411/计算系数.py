a, b, k, n, m = map(int, input().split())
mod = 10007
def comb(k, n):
    Ank = 1
    for i in range(n):
        Ank *= (k - i)
    Ann = 1
    for i in range(1, n+1):
        Ann *= i
    return Ank//Ann

print(((comb(k, n) % mod) * pow(a, n, mod) * pow(b, m, mod)) % mod)