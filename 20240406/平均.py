n = int(input())
a = [[] for _ in range(10)]
for _ in range(n):
    t1, t2 = map(int, input().split())
    a[t1].append(t2)

for i in range(10): a[i].sort()

p = 0
avg_cnt = n//10
for i in range(10):
    if len(a[i]) > avg_cnt:
        p += sum(a[i][:len(a[i])-avg_cnt])
print(p)