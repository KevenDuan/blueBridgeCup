n = 202202011200
cnt = ((n - 14) // 60) * 8 + 1
remain = (n - 14) % 60
tag = [2, 1, 6, 11, 3, 6, 13, 18]
for i in range(len(tag)):
    if remain - tag[i] >= 0:
        cnt += 1
        remain -= tag[i]
    else: break
print(cnt)
