import math
n = int(input())
li = list(map(int, input().split()))
cnt = 0
N = int(1e6) + 20
arr = []
flag = [True] * N
flag[0] = flag[1] = False
for i in range(2, N):
    for j in range(i, N//i):
        flag[i * j] = False
for i in range(len(flag)):
    if flag[i]: arr.append(i)

def bin_s(n):
    l, r = 0, len(arr)
    while l + 1 != r:
        mid = (l + r) // 2
        if arr[mid] > n: r = mid
        else: l = mid
    return l

for i in li:
    t_l = bin_s(i)
    if arr[t_l] == i: continue
    # print('i:', i, f'range({arr[t_l]}, {arr[t_l + 1]})')
    cnt += min(abs(i - arr[t_l]), abs(arr[t_l + 1] - i))

print(cnt)