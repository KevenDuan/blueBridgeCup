n, k = map(int, input().split())
mod = 10**9 + 7
a = sorted(map(int, input().split()))
l, r = 0, n-1
ans = 0
while l <= r:
    if a[l] + a[r] <= k:
        ans += pow(2, r-l, mod)
        l += 1
    else:
        r -= 1
print(ans%mod)