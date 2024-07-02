import sys
input = sys.stdin.readline
A, B = map(int, input().split())
def check(n):
    res = 0
    s = str(n)
    for i in s:
        if i == '0' or i == '6':
            res += 1
        elif i == '8':
            res += 2
    return res

ans = -1
idx = 10**5+10
for i in range(A, B+1):
    res = check(i)
    if res > ans:
        ans = res
        idx = i
print(idx)