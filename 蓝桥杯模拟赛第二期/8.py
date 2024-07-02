n = input()
cnt = 1e5
while cnt > 10:
    cnt = 1
    for i in n:
        if i == '0': continue
        cnt *= int(i)
    print(cnt)
    n = str(cnt)
