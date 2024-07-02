n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else: d[i] += 1

grp = n // 2
cnt_num = 0 # 单数的个数
ans = 0
for k, v in d.items():
    if v == 2: # 默认分好的组
        grp -= 1
        continue
    if v == 1:
        cnt_num += 1
    
for k, v in d.items():
    if v > 2: # v - 2 一定要分配给其他组
        grp -= 1
        ans += min(cnt_num, v - 2)
        grp -= min(cnt_num, v - 2)
        cnt_num -= min(cnt_num, v - 2)
        
# print(d, grp)
if cnt_num == 0:
    ans += grp * 2
else:
    ans += grp
print(ans)