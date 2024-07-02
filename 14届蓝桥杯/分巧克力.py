class food:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        
n, k = map(int, input().split())
li = [] # class:food
s = 0 # 总巧克力面积

for _ in range(n):
    h, w = map(int, input().split())
    s += h * w
    f = food(h, w)
    li.append(f)

l = int((s/k)**0.5) # 初始化边长
tmp = k # 还没有分到巧克力的人数
flag_all = False

while True:
    for i in li: # 读取每个巧克力
        flag = False
        lmt_i = 0
        lmt_j = 0
        for d in range(1, 100001):
            if flag: break
            for g in range(1, 100001):
                # 取最多的巧克力
                if i.h >= g * l:
                    lmt_i = g
                if i.w >= d * l:
                    lmt_j = d
                # 满足条件，终止循环
                if i.h < g * l and i.w < d * l:
                    flag = True
                    break
        tmp -= lmt_i * lmt_j
        if tmp <= 0: # 小朋友全分到了巧克力
            flag_all = True
            break
    if flag_all: break # 结束总循环
    l -= 1

print(l)  
