N, Q = map(int, input().split())
li = list(map(int, input().split()))
ans = []

for i in range(Q):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        for j in range(temp[1], temp[2]+1):
            index = j-1
            li[index] += temp[3]
    else:
        sum = 0
        for j in range(temp[1], temp[2]+1):
            index = j-1
            sum += li[index]
        ans.append(sum)

for i in ans:
    print(i)
