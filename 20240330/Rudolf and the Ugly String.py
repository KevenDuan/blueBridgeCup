for _ in range(int(input())):
    n = int(input())
    a = list(input())
    def check(x):
        if a[x-1] == 'p' and a[x] == 'i' and a[x+1] == 'e': return True
        elif a[x-1] == 'm' and a[x] == 'a' and a[x+1] == 'p': return True
        return False
    ans = 0; i = 1
    while i < n-1:
        if check(i):
            ans += 1
            i += 3
        else: i += 1
    print(ans)
