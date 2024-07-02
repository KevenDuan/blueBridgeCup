def f(n):
    factor = []
    for i in range(2, n+1):
        while n % i == 0:
            n //= i
            factor.append(i)
        if n == 1:
            break
    return factor

print(f(16))