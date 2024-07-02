n, m = map(int, input().split())
x = []
y = []
for i in range(m):
    t_x, t_y = map(int, input().split())
    x.append(t_x)
    y.append(t_y)

print(max((max(x) - min(x)), max(y) - min(y)) + 1)