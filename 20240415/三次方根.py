n = float(input())
l, r = -10000-10, 10000+10
while l + 0.0000001 <= r:
    mid = (l + r) / 2
    if mid * mid * mid >= n:
        r = mid
    else: l = mid
print("%.6f" % r)
