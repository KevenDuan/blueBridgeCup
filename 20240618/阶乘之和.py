a = [1]
for i in range(2, 51):
    a.append(a[-1] * i)

n = int(input())
s = 0
for _ in range(n):
    s += a[_]
print(s)