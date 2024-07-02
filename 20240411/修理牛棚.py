m, s, c = map(int, input().split())
a = [0] + sorted(int(input()) for _ in range(c))
diff = [0] * 201
for i in range(1, c+1):
    diff[i] = a[i] - a[i-1]
diff[1] = 1
diff.sort(reverse=True)
for i in range(min(m-1, c)):
    diff[i] = 1

print(sum(diff))