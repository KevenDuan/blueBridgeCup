import sys
from queue import PriorityQueue
n, m = map(int, input().split())
a = list(map(int, input().split()))
def check(li):
    cnt, ans = 0, 0
    for i in range(len(li)):
        if li[i] > 0:
            cnt += 1
            ans += li[i]
        if cnt > m: return 0
    if cnt <= m: return ans

prex = [a[0]]
for i in range(1, n):
    if prex[-1] < 0 and a[i] < 0:
        prex[-1] += a[i]
    elif prex[-1] < 0 and a[i] > 0:
        prex.append(a[i])
    elif prex[-1] > 0 and a[i] > 0:
        prex[-1] += a[i]
    elif prex[-1] > 0 and a[i] < 0:
        prex.append(a[i])
prex = [0] + prex + [0]
# print(prex) #
tmp = check(prex)
# print(tmp) #
if tmp:
    print(tmp)
    sys.exit()
pq = PriorityQueue()
for i in range(1, len(prex)-1):
    pq.put([abs(prex[i]), i])
while pq.qsize() > 0:
    v, i = pq.get()
    prex[i] += prex[i-1] + prex[i+1]
    prex[i-1] = prex[i+1] = 0
    pq.put([prex[i], i])
    # print(prex)
    tmp = check(prex)
    if tmp:
        print(tmp)
        sys.exit()



