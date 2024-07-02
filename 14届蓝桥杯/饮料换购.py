n = int(input())
ans = n
while n >= 3:
    n -= 3
    ans += 1
    n += 1
print(ans)
