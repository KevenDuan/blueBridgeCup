for _ in range(int(input())):
    a, b, p = map(int, input().split())

    def ksm(a, b, p):
        ans = 1
        while b:
            if b & 1:
                ans *= a % p
            a *= a % p
            b >>= 1
        return ans % p

    print(ksm(a, b, p))