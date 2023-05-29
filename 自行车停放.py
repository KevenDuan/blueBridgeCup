n = int(input())
x = int(input())
li = [x]
for i in range(n-1):
  temp = list(map(int, input().split()))
  iex = li.index(temp[1])
  if temp[2] == 0:
    li.insert(iex, temp[0])
  else: li.insert(iex+1, temp[0])

for i in li:
  print(i, end=' ')
