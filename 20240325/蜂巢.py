d1, p1, q1, d2, p2, q2 = map(int, input().split())
def move(x, y, d, p):
    if d == 0: x -= p
    elif d == 3: x += p
    elif d == 1: x -= p; y += p
    elif d == 2: y += p
    elif d == 5: y -= p
    else: x += p; y -= p
    return x, y
    
def change(d, p, q):
    x, y = move(0, 0, d, p)
    x, y = move(x, y, (d+2)%6, q)
    return x, y
  
x1, y1 = change(d1, p1, q1)
x2, y2 = change(d2, p2, q2)
dy = abs(y2 - y1)
dx = abs(x2 - x1)
if y2 >= y1 and x2 >= x1:
    print(dx + dy)
elif y1 > y2 and x2 > x1:
    print(max(dx, dy))
elif y1 >= y2 and x1 >= x2:
    print(dx + dy)
else: print(max(dx, dy))
