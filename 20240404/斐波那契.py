def mutiply(A, B):
        n, m = len(A), len(A[0])
        _m, k = len(B), len(B[0])
        C = [[0] * (k) for i in range(n)]
        for i in range(n):
            for j in range(k):
                for d in range(m):
                    C[i][j] += (A[i][d] * B[d][j]) % mod
        return C

while True:
    mod = 10000
    n = int(input())-1
    if n == -2: break
    if n == -1:
        print(0)
        continue
    F = [[1, 1]] # [[f(1), f(2)]]
    P = [[0, 1], [1, 1]]
    while n:
        if n & 1:
            F = mutiply(F, P)
        P = mutiply(P, P) # 自乘
        n >>= 1
    print(F[0][0] % mod)