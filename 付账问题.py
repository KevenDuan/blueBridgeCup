import math
n, s = map(int, input().split())
a = list(map(int, input().split()))
a.sort() # a -> 从小到大的排序的钱
sum = 0 
avg = s / n
for i in range(len(a)):
    if a[i] < s / (n - i):
        s -= a[i]
        sum += math.pow(a[i] - avg, 2)
    else: # 无论怎么样都有钱支付的人
        # 最后的平均值,也是剩下的人需要出的钱 -> cul_avg
        cul_avg = s / (n - i)
        sum += math.pow(cul_avg - avg, 2) * (n - i)
        break

print("%.4f" % math.sqrt(sum / n))
