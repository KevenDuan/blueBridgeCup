n = int(input())
mmin, mmax = -1, int(1e9 + 10)
for i in range(n):
    a, b = map(int, input().split())
    tmp1 = a / b; tmp2 = a / (b + 1)
    if tmp1 < mmax: mmax = tmp1
    elif tmp2 > mmin: mmin = tmp2
print(f'{int(mmin) + 1} {int(mmax)}')
