n, m, k, x = map(int, input().split())
cnt = pow(10, k, n)
print((x + cnt*m) % n)