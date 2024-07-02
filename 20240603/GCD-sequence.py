from math import gcd
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n - 1):
        b.append(gcd(a[i], a[i + 1]))
        
    print(b)