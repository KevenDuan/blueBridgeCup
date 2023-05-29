a, b, c = map(int, input().split())
if (a + b) % 3 == 0 or (a + c) % 3 == 0 or (b + c) % 3 == 0:
    print('yes')
else: print('no')
