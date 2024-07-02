for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    idx = (n+1)//2 - 1
    ans = a[idx] + 1
    cnt = 0
    for i in range(idx, n):
        if ans > a[i]: cnt += 1
    print(cnt)
