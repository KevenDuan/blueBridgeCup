t = int(input())
for i in range(t):
    N = int(input())
    S = list(input())
    
    li = [None] * 50
    arr = [None] * 50
    li[1] = 1

    for j in range(1, N):
        u, v = map(int, input().split())
        idx = li.index(u)
        if li[idx * 2] == None: li[idx * 2] = v
        else: li[idx * 2 + 1] = v
    
    for i in range(1, len(S) + 1):
        arr[i] = S[li[i] - 1]
    
    flag = False
    # 判断和子节点是否相同
    for i in range(1, len(S) - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            flag = True
            break
    for i in range(1, len(S) + 1):
        if arr[i] == arr[i * 2]:
            if arr[i * 2] == arr[i * 4] or arr[i * 2] == arr[i * 4 + 1]:
                flag = True
                break
        elif arr[i] == arr[i * 2 + 1]:
            if arr[i] == arr[(i * 2 + 1) * 2] or arr[i] == arr[(i * 2 + 1) * 2 + 1]:
                flag = True
                break
        
    if flag: print("NO")
    else: print("YES")

