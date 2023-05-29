n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i1 in range(n):
    for i2 in range(i1, n):
        for j1 in range(m):
            for j2 in range(j1, m):
                sum = 0
                for i in range(i1, i2+1):
                    for j in range(j1, j2+1):
                        sum += arr[i][j]
                if sum <= k: ans += 1

print(ans)
