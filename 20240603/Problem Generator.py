for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(input())
    cnt = [0] * 7
    for i in a:
        cnt[ord(i) - ord('A')] += 1
    ans = 0
    for i in cnt:
        if i < m:
            ans += m - i
    print(ans) 