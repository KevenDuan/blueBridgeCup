n = int(input())
def f(n):
    ans = 0
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            ans += 1
            while n % i == 0:
                n //= i
    if n > 1:
        ans += 1
    return ans

print(f(n))