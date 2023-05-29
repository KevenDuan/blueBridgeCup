T = int(input())
for i in range(T):
    n = int(input())
    cnt = [0] + list(map(int, input().split()))
    scnt = [0] * (n + 1)
    for j in range(1, n + 1):
        scnt[j] = scnt[j - 1] + cnt[j]
    scnt.sort()
    mmax = scnt[1] - scnt[0]
    for k in range(2, len(scnt)):
        if mmax < scnt[k] - scnt[k - 1]:
            mmax = scnt[k] - scnt[k - 1]
    print(mmax)
