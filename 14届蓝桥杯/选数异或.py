# begain:18:00 end:18:25
n, m, x = map(int, input().split())
li = [0] + list(map(int, input().split()))
temp = []
for i in range(m):
    flag = False
    l, r = map(int, input().split())
    for j in range(l, r+1):
        for k in range(j+1, r+1):
            if li[j] ^ li[k] == x:
                flag = True
    if flag: temp.append('yes')
    else: temp.append('no')
            
for i in temp:
    print(i)
