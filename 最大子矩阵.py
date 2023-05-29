n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
lmt = int(input())
def check(li, lmt):
    if max(li) - min(li) <= lmt:
        print(li)
        return True
    else: return False

left = 0
right = 1000010

while left < right:
    flag = False
    mid = (left + right) // 2
    for i1 in range(n):
        for i2 in range(i1, n):
            for j1 in range(m):
                for j2 in range(j1, m):
                    # 判断子矩阵面积是否为mid
                    if (i2 - i1 + 1) * (j2 - j1 + 1) != mid: continue
                    temp = []
                    
                    # 存子矩阵元素到temp
                    for i in range(i1, i2+1):
                        for j in range(j1, j2+1):
                            temp.append(arr[i][j])

                    # 判断稳定度
                    if check(temp, lmt): flag = True

    if flag: left = mid + 1
    else: right = mid

print(left)
