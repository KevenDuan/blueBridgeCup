data = ['2', '0', '1', '9']
ans = 0
n = int(input())
for i in range(1, n+1):
    li = list(str(i))
    flag = False
    for j in li:
        if j in data:
            flag = True
            break
    if flag:
        ans += i

print(ans)
