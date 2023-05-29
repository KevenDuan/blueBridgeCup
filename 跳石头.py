import itertools

def distance(li):
    a = [0]
    b = []
    for i in li:
        a.append(i)
    a.append(l)
    for i in range(1, len(a)):
        b.append(a[i] - a[i - 1])
    return b # The list return distance between stones

l, n, m = map(int, input().split())
li = [] # The distance from stone and stone
for _ in range(n):
    li.append(int(input()))

c = itertools.combinations(li, n - m)
"""
tmp = list(c)

mmax = []
for i in range(len(tmp)):
    mmax.append(min(distance(tmp[i])))

print(max(mmax))
"""
mmax = []
for i in c:
    mmax.append(min(distance(i)))

print(max(mmax))
    
