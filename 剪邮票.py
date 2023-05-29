from queue import *
def bfs():
    summ = 0
    vis = [0] * 5
    q = Queue()
    q.put(a[0])
    vis[0] = 1
    while not q.empty():
        x = q.get()
        summ += 1
        for i in range(5):
            if vis[i] == 0:
                for j in (-1, 1, 5, -5):
                    if x + j == a[i]:
                        q.put(a[i])
                        vis[i] = 1
    if summ == 5: return True
    else: return
    
def perm(sta, end):
    global p
    if sta == 5: # 判断连通性
        if bfs() == True:
            p += 1
    else:
        for i in range(sta, end + 1):
            a[sta], a[i] = a[i], a[sta]
            perm(sta + 1, end)
            a[i], a[sta] = a[sta], a[i]

a = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]
p = 0
# 排列(11中选取5个邮票) -> 手写排列
perm(0, 11)
# 对排列出来的所有情况求组合
ans = p // 120
print(ans)
