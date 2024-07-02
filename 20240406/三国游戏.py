n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_ = sorted([A[i]-B[i]-C[i] for i in range(n)], reverse=True)
B_ = sorted([B[i]-A[i]-C[i] for i in range(n)], reverse=True)
C_ = sorted([C[i]-A[i]-B[i] for i in range(n)], reverse=True)

prex_A, prex_B, prex_C = [0], [0], [0]
for i in range(n):
    prex_A.append(prex_A[-1] + A_[i])
    prex_B.append(prex_B[-1] + B_[i])
    prex_C.append(prex_C[-1] + C_[i])
    
def check(li):
    l, r = 0, len(li)
    while l + 1 != r:
        mid = (l + r) // 2
        if li[mid] > 0: l = mid
        else: r = mid
    return l
ans = max(check(prex_A), check(prex_B), check(prex_C))
if ans == 0: print(-1)
else: print(ans)