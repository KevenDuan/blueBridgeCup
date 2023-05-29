n, m, k = map(int, input().split())
Di = [0] + list(map(int, input().split()))
T = [0] # 记录上车的时刻
sta = [0] # 出发的站点
end = [0] # 下车的站点

def time_max():
    # 返回每一站最晚上车的人的时刻
    dic = {}
    for i in range(1, n):
        dic[i] = -1
    for i in range(1, len(sta)):
        if T[i] > dic[sta[i]]:
            dic[sta[i]] = T[i]
    return dic

# 读取输入的数据
for _ in range(m):
    a, b, c = map(int, input().split())
    T.append(a)
    sta.append(b)
    end.append(c)

# 记录每一站车上的人数
psum = [0] * (n + 1)
for i in range(1, n):
    for j in range(1, len(sta)):
        if sta[j] <= i < end[j]:
            psum[i] += 1

# 贪心：在车上人最多的路段消耗氮气
li = []
for i in range(len(psum) - 1):
    li.append([psum[i], Di[i], i])
li.sort(reverse = True)
# li记录[车上的人数, Di, i] -> 从大到小的顺序
t = 0
while k > 0:
    # Di大于1则消耗氮气
    if li[t][1] > 1:
        Di[li[t][2]] -= 1
        k -= 1
    else: t += 1

time = 0
dic = time_max()
ti = [0] # 记录每一站花的时间
for i in range(1, n):
    if dic[i] > time:
        time = dic[i]
    time += Di[i]
    ti.append(time)

all_ti = 0 # 总旅游时间
for i in range(1, len(sta)):
    # 到达终点的时刻 - 上车的时刻
    all_ti += ti[end[i]-1] - T[i]

print(all_ti)
