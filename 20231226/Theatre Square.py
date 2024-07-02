n, m, a = map(int, input().split())

def f(a, b):
    l, r = 0, a
    while l + 1 != r:
        m = (l + r) // 2
        if b * m < a: l = m
        else: r = m
    return r

ans = f(n, a) * f(m, a)
print(ans)
