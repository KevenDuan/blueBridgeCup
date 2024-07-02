n = int(input())
li = []; flag = True
for i in range(n):
    a, b, g, k = map(int, input().split())
    li.append((a, b, g, k))
x, y = map(int, input().split())
for i in range(len(li) - 1, -1, -1):
    a, b, g, k = li[i]
    if a <= x <= a + g - 1 and b <= y <= b + k - 1:
        flag = False
        print(i + 1)
        break
if flag: print(-1)
