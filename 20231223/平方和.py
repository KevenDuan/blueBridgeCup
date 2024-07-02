n = int(input())
# ans = (n * (n + 1) * ((2 * n) + 1)) / 6
# print(int(ans))
cnt = 0
for i in range(1, n+1):
    cnt += i * i
print(cnt)