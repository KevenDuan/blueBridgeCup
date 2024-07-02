n = int(input())
ans = 0x3f3f3f3f
for _ in range(3):
    num, price = map(int, input().split())
    ans = min(ans, ((n + num - 1) // num) * price)
print(ans)