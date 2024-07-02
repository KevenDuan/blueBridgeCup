cnt = 1
res = 1
for i in range(2, 500):
    cnt += i
    res += cnt
    if res > 20230610:
        print(i, res)
        break
# 494