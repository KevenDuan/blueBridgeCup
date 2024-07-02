def dis(a, b, c, d):
    return (a - c) ** 2 + (b - d) ** 2

n = int(input())
x = [0] * n
y = [0] * n
sp = set()
cnt = {}

for i in range(n):
    x[i], y[i] = map(int, input().split())
    sp.add((x[i], y[i]))

ans = 0
line = 0

for i in range(n):
    for j in range(n):
        if j != i:
            d = dis(x[i], y[i], x[j], y[j])
            ans += cnt.get(d, 0)
            cnt[d] = cnt.get(d, 0) + 1

            dx = (x[i] << 1) - x[j]
            dy = (y[i] << 1) - y[j]

            if (dx, dy) in sp:
                line += 1

    cnt.clear()

print(ans - (line >> 1))