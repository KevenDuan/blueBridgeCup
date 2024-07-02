for _ in range(int(input())):
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))
    cnt1 = defaultdict(int)
    cnt2 = defaultdict(int)
    cnt3 = defaultdict(int)
    cnt4 = defaultdict(int)
    ans = 0
    for i in range(0, n-2):
        x, y, z = a[i], a[i+1], a[i+2]
        ans += cnt1[(x, y)] + cnt2[(x, z)] + cnt3[(y, z)] - 3 * cnt4[(x, y, z)]
        cnt1[(x, y)] += 1
        cnt2[(x, z)] += 1
        cnt3[(y, z)] += 1
        cnt4[(x, y, z)] += 1
    print(ans)