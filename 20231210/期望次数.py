n, m = map(int, input().split())
p = [0] + list(map(int, input().split()))
cnt = 0
pi = 0
for i in range(1, n + 1):
    pi += p[i]
print(pi)
