n = int(input())
a = [0] + list(map(int, input().split()))
x = [0] * (n + 1)
x[2] = a[1]
x[3] = a[2] - a[1]
for i in range(4, n+1):
    x[i] = a[i-1] - a[i-2] + x[i-3]
x[n-1] = min(x[n-1], 0)
x[n] = min(x[n], a[n] - x[n-1])
x[n-2] = min(x[n-2], a[n-1]-a[n])
for i in range(n-3, 0, -1):
    x[i] = min(x[i], a[i+1]-a[i+2]+x[i+3])
x[n-2] = min(x[n-2], a[n-1]-a[n])
print(*x[1:])
    
