n = int(input())
a = list(map(int, input().split()))
# a.sort()
def get_length(x):
    cnt = 0
    while x != 0:
        if x&1: cnt += 1
        x >>= 1
    return cnt

num_cnt = [0] * (32)
for i in range(n):
    x = a[i]
    # print(x)
    for j in range(32):
        if x&1: num_cnt[j] += 1
        x >>= 1
        if x == 0: break

ans = 0
for i in num_cnt:
    ans += (1 + (i-1))*(i-1)//2
print(ans)