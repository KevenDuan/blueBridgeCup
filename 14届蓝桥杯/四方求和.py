import math

def getSum(li):
    sum = 0
    for i in li:
        sum += i*i
    return sum

n = int(input())
li = []
for i in range(4):
    num = int(math.sqrt(n))
    li.append(num)
    if getSum(li) == n:
        break
    n -= num * num
li.sort()
for i in li:
    print(i, end=' ')
