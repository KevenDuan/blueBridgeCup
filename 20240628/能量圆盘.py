n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    if i not in d: d[i] = 1
    else: d[i] += 1

li = []
for k, v in d.items():
    li.append((v, k))
li.sort(reverse=True)

tag = li[0][1]
val = li[0][0]
print(n - val)