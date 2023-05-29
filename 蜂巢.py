def walk(d, p, q):
    if d == 0:
        return -2 * p + q, q
    elif d == 1:
        return -p + 2 * q, p
    elif d == 2:
        return p + q, p - q
    elif d == 3:
        return 2 * p - q, -q
    elif d == 4:
        return p - 2 * q, -p
    elif d == 5:
        return -p - q, -p + q

d1, p1, q1, d2, p2, q2 = map(int, input().split())
x1, y1 = walk(d1, p1, q1)
x2, y2 = walk(d2, p2, q2)
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx >= dy: print((dx + dy)//2)   
else: print(dy)
