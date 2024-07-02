n, k = map(int, input().split())
arr = [0] * (n + 2)
for _ in range(k):
    l, r = map(int, input().split())
    arr[r + 1] -= 1
    arr[l] += 1

prex = [0]
for i in range(1, n + 1):
    prex.append(prex[-1] + arr[i])
prex = sorted(prex[1:])
print(prex[n // 2])