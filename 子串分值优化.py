n = input()
latter = [[-1] for _ in range(26)]
for i in range(len(n)):
    latter[ord(n[i])-97].append(i)
for i in latter:
    i.append(len(n))
# 贡献度判断
res = 0
for i in latter:
    if len(i) == 2:
        continue
    for j in range(1, len(i)-1):
        res += (i[j] - i[j-1]) * (i[j+1] - i[j])

print(res)
