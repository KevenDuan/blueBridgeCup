import sys
sys.setrecursionlimit(1000000)
def quickSort(li:list):
    l = len(li); m = l // 2
    if l == 1 or l == 0: return li
    left = []; right = []
    for i in range(l):
        if i == m: continue
        if li[i] < li[m]: left.append(li[i])
        else: right.append(li[i])
    return quickSort(left) + [li[m]] + quickSort(right)

n = input()
li = list(map(int, input().split()))
print(*quickSort(li))
