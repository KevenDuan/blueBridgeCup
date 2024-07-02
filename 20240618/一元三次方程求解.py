def solve(x):
    return a * (x ** 3) + b * (x ** 2) + c * x + d

def check(ans):
    pass

a, b, c, d = map(int, input().split())
l, r = -100, 100
while l + 0.0001 <= r:
    mid = (l + r) / 2
    if check(mid): l = mid
    else: r = mid
