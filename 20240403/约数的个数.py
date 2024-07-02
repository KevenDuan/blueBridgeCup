n = int(input())
a = list(map(int, input().split()))

def judge(N):
    result = []
    for i in range(2, N+1):
        while N % i == 0:
            N //= i
            result.append(i)
        if N == 1:
            break
    return result

for i in range(n):
    res = judge(a[i])
    d = {}
    for i in res:
        if i not in d:
            d[i] = 1
        else: d[i] += 1
    
    ans = 1
    for k, v in d.items():
        ans *= (1 + v)
    print(ans)