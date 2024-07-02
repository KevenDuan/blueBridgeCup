t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    cnt = a + (b+3-1) // 3
    if b % 3 != 0:
        c -= (b//3 + 1) * 3 - b
    cnt += (c + 3 - 1)//3
    if c < 0: print(-1)
    else: print(cnt)
