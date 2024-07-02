n = int(input())
a = input()
d = [0, 0, 0, 0]
mod = 10**9 + 7
for i in range(n):
    if a[i] == 'A': d[0] += 1
    elif a[i] == 'C': d[1] += 1
    elif a[i] == 'G': d[2] += 1
    else: d[3] += 1

value_max = max(d)
cnt = 0
for i in range(len(d)):
    if d[i] == value_max: cnt += 1

print(pow(cnt, n, mod))
