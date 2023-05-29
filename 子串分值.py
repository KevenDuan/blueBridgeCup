str = input()
sum = 0
for i in range(len(str)):
    temp = ''
    for j in range(i, len(str)):
        temp += str[j]
        for k in temp:
            if temp.count(k) == 1:
                sum += 1

print(sum)
