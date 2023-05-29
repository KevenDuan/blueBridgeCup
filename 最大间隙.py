n = int(input())
l = list(map(int, input().split()))
temp = []
for i in range(len(l)-1):
    temp.append(l[i+1] - l[i])

print(max(temp))
