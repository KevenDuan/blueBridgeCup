def check(k):
    return (k & (k>>1)) == 0

def check_p(a, b):
    return (a & b) == 0

def get_cnt(k):
    res = 0
    while k:
        res += k&1
        k >>= 1
    return res
    
n, m = map(int, input().split())
mp = 0; ST = 1<<m; ans = 0
f = [[0] * ST for _ in range(n+1)]

for i in range(1, n+1):
    a = int(''.join(list(input().split())), 2)
    mp |= a

    for k in range(ST):
        if check(k) and check_p(mp, k):
            cnt = get_cnt(k)
            for j in range(ST):
                if check(j) and check_p(k, j):
                    f[i][k] = max(f[i-1][j] + cnt, f[i][k])
            ans = max(ans, f[i][k])
    
    mp = 0
print(ans)