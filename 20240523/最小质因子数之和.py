def get_prime(n):
    prime = [0] * (n+1)
    for i in range(2, n+1):
        if prime[i] == 0:
            f[i] = i
            if i * i >= n: continue
            for j in range(i+i, n+1, i):
                prime[j] = 1
                f[j] = min(f[j], i)
    f[1] = 0

    for i in range(2, n+1):
        f[i] += f[i - 1]   

N = int(3e6) + 100
f = [0x3f3f3f3f] * N
get_prime(N-3)
for _ in range(int(input())):
    n = int(input())            
    print(f[n])