n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# 先将数组排序
a.sort()
b.sort()
c.sort()

# 对于每个 b[j]，找出满足 a[i] < b[j] 和 b[j] < c[k] 的 i 和 k 的位置
i, k = 0, 0
count = 0
for j in range(n):
    while i < n and a[i] < b[j]:
        i += 1
    while k < n and c[k] <= b[j]:
        k += 1
    count += i * (n-k)

print(count)
