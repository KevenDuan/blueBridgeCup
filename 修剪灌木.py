N = int(input())
li = []
if N % 2 == 0: # 偶数课树
    for i in range(0, int(N//2)):
        j = i
        sum = 0
        flag = True
        while True:
            if flag:
                j += 1
                sum += 1
                if j == (N-1):
                    flag = False
            
            if not flag:
                j -= 1
                sum += 1
                if j == i:
                    break      
        li.append(sum)
    li.extend(li[::-1])
    for i in li:
        print(i)

else: # 质数课数
    temp = []
    for i in range(0, int(N//2)+1):
        j = i
        sum = 0
        flag = True
        while True:
            if flag:
                j += 1
                sum += 1
                if j == (N-1):
                    flag = False
            
            if not flag:
                j -= 1
                sum += 1
                if j == i:
                    break
        li.append(sum)
    temp = li[::-1]
    del temp[0]
    li.extend(temp)
    for i in li:
        print(i)


