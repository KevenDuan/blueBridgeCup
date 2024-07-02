def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    x = [0] * (n + 1)
    res = '2'
    for i in range(2):
        x[1], x[2] = i, a[1] - i
        if x[2] < 0: continue
        x[3] = a[2] - a[1]
        for k in range(4, n+1):
            x[k] = a[k-1] - a[k-2] + x[k-3]
            if x[k] < 0 or x[k] > 1: break
        if x[n-1] + x[n] == a[n]:
            x = list(map(str, x))
            res = min(res, ''.join(x[1:]))

    print(*list(res))
main()
