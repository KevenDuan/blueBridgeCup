import sys
input = sys.stdin.readline

def floyd(k):
    for _ in range(n):
        for __ in range(n):
            dp[_][__] = min(dp[_][__], dp[_][k] + dp[k][__])
            
n, k = map(int, input().split())
k_a = list(map(int, input().split()))
dp = [list(map(int, input().split())) for _ in range(n)]
T = int(input())

for _ in range(n):
    for __ in range(n):
        if dp[_][__] == -1: dp[_][__] = 0x3f3f3f3f
        
ans = 0; d = {}
for _ in k_a: d[_-1] = 1
for _ in range(n):
    if _ in d: floyd(_)

for __ in range(T):
    l = list(map(int, input().split()))[:-1]
    for _ in l: d[_-1] = 1
    
    for _ in l:
        d[_-1] = 1
        floyd(_-1)
    
    for _ in range(n):
        if _ not in d: continue
        for __ in range(n):
            if __ not in d: continue
            if dp[_][__] > 10**9: continue
            ans += dp[_][__]

print(ans)