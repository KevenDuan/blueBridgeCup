n = int(input())
li = list(map(int, input().split()))
N = 100010
cnt = [0] * N; scnt = [0] * N
for i in range(n):
    cnt[li[i]] += 1

cnt[0] = scnt[0]
for i in range(1, N):
    scnt[i] = scnt[i - 1] + cnt[i]

def check(v, old):
    more = scnt[N - 1] - scnt[v]
    fewer = scnt[v] - cnt[v]
    if v != old:
        fewer -= 1
    if fewer >= more: return True
    else: return False
    
res = ""
for i in range(len(li)):
    l, r = li[i] - 1, N
    while l + 1 != r:
        mid = (l + r) >> 1
        if check(mid, li[i]):
            r = mid
        else: l = mid
    res += str(r - li[i]) + ' '

print(res)
