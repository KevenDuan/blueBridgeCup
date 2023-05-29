import math
N = int(input())
li = [0] + list(map(int, input().split()))
f = int(math.log(N+1, 2))
bi = []

for i in range(1, f+1):
    cnt = 0
    k = 2**(i-1)
    for j in range(k, k+(2**(i-1))):
        cnt += li[j]
    bi.append(cnt)

bi.append(sum(li[2**f:-1]))

a = max(bi)
print(bi.index(a) + 1)
