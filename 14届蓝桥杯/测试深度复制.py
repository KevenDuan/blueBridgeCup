from copy import deepcopy
arr = [1, 2, 3, 4]
arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = [[1, 2, 3], [4, 5, 6]]
# 一维数组深复制
temp = arr.copy()
temp.append(5)

# 二维数组浅复制
temp1 = arr1.copy()
temp1[1][2] = 7

# 二维数组深复制
temp2 = deepcopy(arr2)
temp2[1][2] = 7

print(arr, temp)
print(arr1, temp1)
print(arr2, temp2)
