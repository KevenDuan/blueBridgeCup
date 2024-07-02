n, m, k = map(int, input().split())
a = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == '1':
            cnt += 1

for i in range(k+1):
    if 3 * i + 2 * (k-i) == cnt:
        print(i, k-i)
        break