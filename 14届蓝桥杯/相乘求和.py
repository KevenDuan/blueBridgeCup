n = int(input())
li = list(map(int, input().split()))
"""
time complexity: O(n)
"""
cnt = 0
num = 0
for i in range(n):
    num += li[i]

for i in range(n):
    num -= li[i]
    cnt += li[i] * num

print(cnt)
