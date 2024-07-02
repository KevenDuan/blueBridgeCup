import sys
D1, C, D2, P, N = map(float, input().split())
N = int(N)
Di = [0] # distance
Pi = [P] # price
for _ in range(N):
    d, p = map(float, input().split())
    Di.append(d); Pi.append(p)
Di.append(D1); Pi.append(0)
a = [0] * (N + 1) # 记录每个加油站加的油
DIS = C * D2 # 满箱油能行驶的距离
remain = 0 # 剩余的油量
i = 0
while i <= N:
    to_next = Di[i + 1] - Di[i]
    if to_next > DIS: print('No Solution'); sys.exit()
    for k in range(i + 1, N + 2):
        if Pi[k] <= Pi[i]: to_k = Di[k] - Di[i]; break
    if DIS >= to_k: # 一箱油可以到达k站
        oil = to_k / D2 # 到达k站需要的油
        if remain > oil: # 剩余的油量可以到k站
            remain -= oil
        else: a[i] = oil - remain # 实际加油量
        i = k # 移动到k站
    else: # 不能到达k站，加满油去下一站
        a[i] = C - remain
        remain = C - (to_next/D2)
        i += 1

cost = 0
for i in range(N + 1): cost += a[i] * Pi[i]
print('%.2f' % cost)
