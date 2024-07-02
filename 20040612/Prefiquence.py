for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()

    def check(ans):
        tmp = a[:ans]
        i = 0
        for j in range(m):
            if i == len(tmp): return True
            if b[j] == tmp[i]: i += 1
            
        if i == len(tmp): return True
        else: return False

    l, r = 0, n + 1
    while l + 1 != r:
        mid = (l + r) // 2
        if check(mid):
            l = mid
        else: r = mid
    print(l)