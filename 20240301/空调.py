N = int(input())
p = [0] + list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
for i in range(1, N + 1): a[i] = p[i] - a[i]
diff = [0]
a1, b1 = 0, 0
for i in range(1, N + 1):
    diff.append(a[i] - a[i - 1])
    if diff[i] > 0: a1 += diff[i]
    else: b1 += diff[i]
print(max(abs(a1), abs(b1)))