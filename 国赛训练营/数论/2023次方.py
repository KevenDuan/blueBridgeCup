from math import gcd
import sys
sys.setrecursionlimit(10**5)

def Ehi(x):
    cnt = 0
    for i in range(1, x):
        if gcd(i, x) == 1:
            cnt += 1
    return cnt

def dfs(a, b):
    if b > fn:
        b = b % fn + fn
    b = pow(a, b, fn)
    
    if a == 3:
        print(b)
        return
    
    dfs(a-1, b)
    
mod = 2023
fn = Ehi(mod)
dfs(2022, 2023) # 1089
print(pow(2, 1089, mod)) # 869
