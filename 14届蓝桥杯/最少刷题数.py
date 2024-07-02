n = int(input())
li = list(map(int, input().split()))

def check(d, i):
    less = 0
    more = 0
    for val in range(n):
        if val == i: continue
        elif li[i] + d > li[val]: less += 1
        elif li[i] + d < li[val]: more += 1
    if more > less: return True
    else: return False
        
for i in range(n):
    left = 0
    right = 100010
    while left < right:
        mid = (left + right) // 2
        if check(mid, i): left = mid + 1
        else: right = mid
    print(left, end = ' ')
