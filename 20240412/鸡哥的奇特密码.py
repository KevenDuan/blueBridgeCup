s = list(input())
flag = True
ans = []
for i in s:
    if i == 'Q':
        flag = True
        ans.append(i)
    elif i == 'L' and flag:
        flag = False
        ans.append(i)
print(''.join(ans))