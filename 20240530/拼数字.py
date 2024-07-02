from itertools import permutations
n, m = map(int, input().split())
s = '2' * n + '3' * m
ans = []

for i in permutations(s):
    num = int(''.join(i))
    if num % 2023 == 0:
        ans.append(num)

ans.sort()
if len(ans) == 0:
    print(-1)
else: print(ans[-1])