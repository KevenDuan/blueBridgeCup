def solve(x):
    res = []
    for i in range(2, x + 1):
        while x % i == 0:
            res.append(i)
            x //= i
    return res

d = {}
for i in range(1, 100 + 1):
    res = solve(i)
    for i in res:
        if i not in d:
            d[i] = 1
        else: d[i] += 1

ans = 1
for k, v in d.items():
    ans *= (v + 1)
print(ans)