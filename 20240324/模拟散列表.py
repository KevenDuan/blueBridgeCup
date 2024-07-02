n = int(input())
d = {}
for _ in range(n):
    a, b = input().split()
    if a == 'I':
        if b not in d: d[b] = 1
    else:
        if b in d:
            print('Yes')
        else: print('No')
