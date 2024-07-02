l, r = map(int, input().split())
cnt = 0
for i in range(l, r+1):
    for j in str(i):
        if '2' == j: cnt += 1
print(cnt)
