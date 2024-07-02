n = int(input())
s = [0] * (n + 1)
e = [0] * (n + 1)
a = []
for _ in range(1, n + 1):
    si, ai, ei = map(int, input().split())
    s[_] = si + ai
    e[_] = ei
    a.append((s[_] + e[_], _))
a.sort()
ans = 0
now_time = 0
for i in range(n):
    time, id = a[i]
    now_time += s[id] # 加上答疑的时间
    ans += now_time
    now_time += e[id] # 加上离场的时间
print(ans)
    