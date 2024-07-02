n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
tot = 0 # 有效升级次数
for i in range(n):
    tot += (a[i][0] + a[i][1] - 1) // a[i][1]
tot = min(m, tot)

def check(ans):
    s = 0
    for i in range(n):
        if a[i][0] >= ans:
            s += (a[i][0] - ans) // a[i][1] + 1
    return s >= tot
# 二分筛选出最小可加的攻击力
l, r = 0, 10**6 + 5
while l + 1 != r:
    mid = (l + r) // 2
    if check(mid): l = mid
    else: r = mid

ans = 0
for i in range(n):
    t = (a[i][0] - l) // a[i][1] + 1 # 技能i对总次数的贡献
    if t < 0 or a[i][0] < l: continue # 一直没有升级过该技能
    if a[i][0] - a[i][1] * (t - 1) == l:
        t -= 1
    ans += t * a[i][0] - (t * (t - 1) // 2 * a[i][1]) # 等差数列求n项和公式
    tot  -= t
print(ans + tot * l)