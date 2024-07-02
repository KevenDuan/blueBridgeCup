from math import gcd
for _ in range(int(input())):
    x = int(input())
    m = 0
    ans = 0
    for y in range(1, x):
        if m <= gcd(x, y) + y:
            m = gcd(x, y) + y
            ans = y
    print(ans)