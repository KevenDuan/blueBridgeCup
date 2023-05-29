# 二分法求（符合单调性）
def check(x):  # 定义一个函数
    x //= 5
    res = 0
    while x > 0:
        res = res + x
        x //= 5
    return res


k = int(input())
left = 1
right = int(10e18)

while left < right:
    mid = (left + right) //2
    if check(mid) >= k:
        right = mid
    else:
        left = mid + 1
if check(left) == k:
    print(left)
else:
    print(-1)
