from math import gcd

def chk(a, b):
    return gcd(a, b)==1

def main():
    n = 21
    f = [[0] * (n+1) for _ in range(1<<n)]
    mp = [[0] * (n+1) for _ in range(n + 1)]
    
    for i in range(n+1):
        for j in range(n+1):
            if chk(i, j) == 1: mp[i][j] = 1

    f[1][0] = 1

    for i in range(1<<n):
        for j in range(n):
            if i>>j&1: # j在i状态中
                for k in range(n):
                    if i>>k&1 and mp[j+1][k+1]: # k也在i状态中且与j互质
                        f[i][j] += f[i-(1<<j)][k]

    res = 0
    for i in range(1, n):
        res += f[(1<<n)-1][i]
    print(res)
        
    
if __name__ == '__main__':
    main() # 881012367360