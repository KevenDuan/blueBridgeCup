from queue import PriorityQueue
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
t = int(input())
fish_max_num = 0
for i in range(n):
    road_time = sum(c[:i+1])
    if road_time >= t: break
    fish_time = t - road_time
    fish_num = 0
    pq = PriorityQueue()
    for j in range(i+1):
        pq.put([-a[j], j])
    while fish_time:
        v, idx = pq.get()
        if v >= 0: break
        fish_num += -v
        pq.put([v + b[idx], idx])
        fish_time -= 1
    fish_max_num = max(fish_max_num, fish_num)
print(fish_max_num)
