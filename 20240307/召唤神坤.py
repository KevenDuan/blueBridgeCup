n = int(input())
a = sorted(map(int, input().split()))
k = a[-1]
mmax = -1
for i in range(n-2):
    mmax = max(mmax, (a[i] + k)//a[i+1])
    print(a[i], a[i+1], (a[i] + k)//a[i+1])
print(mmax)
