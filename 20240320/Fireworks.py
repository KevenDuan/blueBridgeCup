from math import gcd
t = int(input())
for _ in range(t):
    a, b, m = map(int, input().split())
    begin = gcd(a, b)
    end = begin + m
    ans = (end-begin)//a + (end-begin)//b + 2
    print(ans)
