import sys
input = sys.stdin.readline
mod = 10**9 + 7
def main():
    for i in range(int(input())):
        n, k = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        prex = [0]
        for i in range(1, n+1):
            prex.append(prex[-1] + a[i])

        dp = [0] * (n + 1)
        for i in range(n+1):
            dp[i] = (max(dp[i-1], 0) + a[i])
        s = max(dp)
        res = s
        for i in range(1, k):
            s = (s * 2) % mod
            res = (res + s) % mod
        print((res + prex[n]) % mod)

main()
