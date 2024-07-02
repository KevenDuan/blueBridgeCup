n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dire = {}
for _ in range(m):
    if b[_] not in dire: dire[b[_]] = 1