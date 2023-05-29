from copy import deepcopy
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
temp = deepcopy(arr)

for i in range(n):
    for j in range(m):
        if i == 0: # 第一行
            if j == 0: # 第一列
                temp[i][j] = int(sum([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]]) / 4)
            elif j == m-1: # 最后一列
                temp[i][j] = int(sum([arr[i][j], arr[i][j-1], arr[i+1][j-1], arr[i+1][j]]) / 4)
            else:
                temp[i][j] = int(sum([arr[i][j], arr[i][j-1], arr[i][j+1], arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1]]) / 6)
        elif i == n-1:# 最后一行
            if j == 0: # 第一列
                temp[i][0] = int(sum([arr[i][j], arr[i][j+1], arr[i-1][j], arr[i-1][j+1]]) / 4)
            elif j == m-1: # 最后一列
                temp[i][m-1] = int(sum([arr[i][j], arr[i][j-1], arr[i-1][j-1], arr[i-1][j]]) / 4)
            else:
                    temp[i][j] = int(sum([arr[i][j], arr[i][j-1], arr[i][j+1], arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1]]) / 6)
        else:
            if j == 0: # 第一列
                temp[i][j] = int(sum([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1], arr[i-1][j], arr[i-1][j+1]]) / 6)
            elif j == m-1: # 最后一列
                temp[i][j] = int(sum([arr[i][j], arr[i][j-1], arr[i+1][j-1], arr[i+1][j], arr[i-1][j-1], arr[i-1][j]]) / 6)
            else:
                temp[i][j] = int(sum([arr[i][j], arr[i][j-1], arr[i][j+1], arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1], arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1]]) / 9)

for i in temp:
    for j in i:
        print(j, end=' ')
    print()
