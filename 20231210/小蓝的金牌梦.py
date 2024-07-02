import math
n = int(input())
li = list(map(int, input().split()))
def judge(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return True
    return False

c = []
for i in range(1, int(1e5) + 1):
  if not judge(i):
    c.append(i)

arr = [0] * (n + 10)
for i in range(n):
    arr[i + 1] = (arr[i] + li[i])

rst = -1e6
# O(n2) TLE
for j in c:
  for i in range(1, n - j + 2):
      rst = max(rst, arr[i + j -1] - arr[i - 1])

print(rst)