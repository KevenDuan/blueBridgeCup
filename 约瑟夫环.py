n, k, m = map(int, input().split())
li = [i for i in range(1, n+1)]
index = k - 1
while len(li) > 0:
    index = (index + m - 1) % len(li)
    print(li.pop(index))
