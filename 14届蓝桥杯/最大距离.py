n = int(input())
li = [int(i) for i in input().split()]
temp = []
for i in range(len(li)):
    for j in range(len(li)):
        a = li[i] - li[j]
        b = i - j
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        temp.append(a+b)
print(max(temp))
