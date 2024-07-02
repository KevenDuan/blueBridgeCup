import sys
from math import gcd
n = int(input())
a = list(map(int, input().split()))

cnt_ji = 0
for i in range(n):
    if a[i]&1: cnt_ji += 1

if cnt_ji >= 2:
    print(1)
    sys.exit()

s = []

def lcm(a, b):
    return (a*b)//gcd(a, b)

for i in range(n):
    for j in range(i+1, n):
        s.append(lcm(a[i], a[j]))

ans = s[0]
for i in range(1, len(s)):
    ans = gcd(ans, s[i])
print(ans)