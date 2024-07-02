a, b = map(int, input().split())
for _ in range(1, 1000 + 10):
    if _ * 1.9 > a + b * 0.1:
        print(_ - 1)
        break