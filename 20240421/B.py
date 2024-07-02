a = []
for i in range(33):
    a.append(1<<i)
prex = [0]
for i in range(len(a)):
    prex.append(prex[-1]+a[i])
# print(a)
# print(prex)
# print([bin(i) for i in prex])

# for _ in range(1):
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = 0 # 最多可以出现ans个1
    for i in range(1, len(prex)):
        if prex[i] <= k:
            ans = i
    # print('ans:', ans)
    if n == 1:
        print(k, end = ' ')
    else:
        print(prex[ans], end = ' ')
        print(k - prex[ans], end = ' ')
        for i in range(n - 2):
            print(0, end = ' ')
    print()