n, w = map(int, input().split())
arr = [0] * int(2e5 + 10)
darr = [0] * int(2e5 + 10)
flag = 1
lenth = 0
for i in range(n):
    s, t, p = map(int, input().split())
    darr[s] += p; darr[t] -= p
    lenth = max(lenth, t)
for i in range(lenth + 5):
    arr[i] = arr[i - 1] + darr[i]
    if arr[i] > w:
        flag = 0
        break

if flag: print('Yes')
else: print('No')
