import math
arr = []
def fun(x):
    # 为质数输出True
    if x == 1: return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            arr.append(i)
            return False
    else: return True

a, b = map(int, input().split())
if b - a > 300:
    beg = b - 320
else: beg = a + 1
max = 0
for i in range(b, beg - 1, -1):
    if fun(i):
        max = i
        break
if max != 0:
    cnt = 0
    for i in range(b, max, -1):
        if arr[cnt] > a:
            max = i
            break
        cnt += 1
    print(max)
else: print(-1)
