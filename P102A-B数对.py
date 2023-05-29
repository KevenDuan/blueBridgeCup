N, C = map(int, input().split())
li = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if abs(li[i] - li[j]) == C:
             ans += 1

print(ans)
