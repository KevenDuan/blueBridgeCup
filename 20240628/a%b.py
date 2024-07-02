import math
a, b = map(int, input().split())
if b > 0:
    print(a % b)
else:
    q = math.ceil(a / b)
    r = a - b * q
    print(r)