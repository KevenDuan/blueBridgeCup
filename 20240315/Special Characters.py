t = int(input())
for _ in range(t):
    n = int(input())
    if n&1: print('NO')
    else:
        print('YES')
        print('AAB'*(n//2))
