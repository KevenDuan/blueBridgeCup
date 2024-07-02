for _ in range(int(input())):
    n, a, b = map(int, input().split())
    price = 0
    if 2 * a > b:
        price += (n//2) * b
        price += (n%2) * a
    else:
        price += n * a
    print(price)