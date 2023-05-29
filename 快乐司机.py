n, w = map(int, input().split())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

d.sort(key=lambda x: x[1]/x[0], reverse=True)
price = 0
for k in d:
    if w > k[0]:
        w -= k[0]
        price += k[1]
    else:
        price += w * k[1]/k[0]
        break

print("%.1f" % price)