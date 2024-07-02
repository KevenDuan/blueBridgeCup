from queue import PriorityQueue
n, m = map(int, input().split())
q = PriorityQueue()
for _ in range(n):
    A, B = map(int, input().split())
    q.put([-A, B])

cnt, ans = 0, 0
while q.qsize() != 0 and cnt < m:
    A, B = q.get()
    ans += A; cnt += 1
    if -A >= B: A += B
    else: A = 0
    q.put([A, B])
print(-ans)