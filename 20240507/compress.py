def compress(array, n):
    newArr = []
    for i in range(n):
        for j in range(i, n):
            newArr.append(array[i][j])
    return newArr

def unpack(array, n):
    newArr = [[None] * n for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if j >= i:
                newArr[i][j] = array[cnt]
                cnt += 1
            else: newArr[i][j] = newArr[j][i]
    return newArr

n = 3   
A = [[1, 2, 3],
     [2, 4, 5],
     [3, 5, 6]]
a = compress(A, n)
print(a)
b = [5, 6, 7, 8, 9, 1]
B = unpack(b, n)
for i in range(n):
    print(B[i])
