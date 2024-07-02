n, k = map(int, input().split())
li = [0] + list(map(int, input().split()))
add = [0] * (n + 1)
for i in range(1, n + 1):
    add[i] = li[i] + add[i - 1]

mmax = -1
for i in range(1, n - 1):
    tmp = add[i + 2] - add[i - 1]
    if tmp > mmax: mmax = tmp
print(mmax)
