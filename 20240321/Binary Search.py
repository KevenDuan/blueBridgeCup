for _ in range(int(input())):
    n, x = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    def bin_search(x):
        l, r = 1, n+1
        while l + 1 != r:
            m = (l + r) // 2
            if p[m] <= x: l = m
            else: r = m
        return l
    print(1)
    print(p.index(x), bin_search(x))
