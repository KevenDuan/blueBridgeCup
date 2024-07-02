t = int(input())

def f(x):
    for i in range(2, x + 2): # O(1)
        if x % i != 0 and i != x: return i

for i in range(t): # O(1e5)
    cnt = 0
    a, n = map(int, input().split())
    for i in range(2, n + 2, 2): # O(1e16)
        if a == 2 and n % 2 == 0:
            print(n // 2)
            break
        elif a == 2:
            print(n // 2 + 1)
            break
        # print(i, f(i)) # 
        if f(i) == a: cnt += 1
    print(cnt)