import sys
input = sys.stdin.readline
mod = 998244353
n, m, a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for x in range(n-a+1):
    for y in range(m-b+1):
        mmax, mmin = 0, 0x3f3f3f3f
        for i in range(x, x+a):
            for j in range(y, y+b):
                mmax = max(mmax, arr[i][j])
                mmin = min(mmin, arr[i][j])
        ans += (mmax * mmin) % mod
print(ans % mod)