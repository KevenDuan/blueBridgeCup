n = int(input())
arr = list(map(int, input().split()))
left = [arr[0]]
for i in range(1, n):
    while arr[i] in left:
        arr[i] += 1
    left.append(arr[i])

for i in arr:
    print(i, end=' ')
