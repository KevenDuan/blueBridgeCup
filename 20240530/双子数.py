def getPrime(n):
    flag = [0] * (n + 1)
    prime = []
    for i in range(2, n + 1):
        if flag[i] == 0:
            for j in range(i * i, n + 1, i):
                flag[j] = 1
    
    for i in range(2, n + 1):
        if flag[i] == 0:
            prime.append(i)
    
    return prime

n = 5000000
prime = getPrime(n)

ans = 0
for i in range(len(prime)):
    pp = prime[i] * prime[i]
    if pp * pp > 23333333333333: break
    for j in range(i + 1, len(prime)):
        qq = prime[j] * prime[j]
        if qq * pp > 23333333333333: break
        if qq * pp < 2333: continue
        ans += 1
print(ans)