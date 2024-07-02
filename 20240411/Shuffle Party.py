import math
mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    if n == 1: print(1)
    else: print(pow(2, int(math.log2(n)), mod))