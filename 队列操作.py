N = int(input())
arr = []
for i in range(N):
    li = list(map(int, input().split()))
    if li[0] == 1:
        arr.append(li[1])
    elif li[0] == 2:
        if len(arr) == 0:
            print('no')
        else:
            print(arr[0])
            del arr[0]
    elif li[0] == 3:
        print(len(arr))
