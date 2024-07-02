n = int(input())
arr = [0] + list(map(int, input().split()))
scnt = [0] * (n + 1) # 前缀和
pcnt = [1] * (n + 1) # 前缀积
for i in range(1, n + 1):
    scnt[i] = scnt[i - 1] + arr[i]
    pcnt[i] = pcnt[i - 1] * arr[i]

ans = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if scnt[j] - scnt[i - 1] == pcnt[j] // pcnt[i - 1]:
            ans += 1

print(ans)
