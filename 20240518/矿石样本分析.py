n, K = map(int, input().split())
a = list(map(int, input().split()))
d = {} # hash表
for i in range(n):
    # key:该矿石的属性；value:该矿石的下标
    if i not in d: d[a[i]] = i

def min_time(i, j): # 模拟机器人的各种情况取最小挖矿时间
    return min(max(i+1, j+1), max(n-i, n-j), max(n-i, j+1), max(n-j, i+1))

t = 0x3f3f3f3f
for i in range(n):
    # 在hash表中找是否有矿石和该矿石属性之和为K且两矿石属性不等
    if K-a[i] in d and K-a[i] != a[i]:
        j = d[K-a[i]] # 获取与该矿石匹配矿石的下标
        t = min(t, min_time(i, j))
        
if t > 1e9: print(-1)
else: print(t)