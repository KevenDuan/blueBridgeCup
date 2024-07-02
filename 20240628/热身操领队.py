from queue import PriorityQueue
dq_1 = PriorityQueue()
dq_2 = PriorityQueue()
def add(num):
    if dq_1.qsize() == 0:
        dq_1.put(-num)
    elif num >= -dq_1.queue[0]:
        dq_2.put(num)
    else: dq_1.put(num)
    
    if dq_1.qsize() > dq_2.qsize() + 1:
        dq_2.put(-dq_1.get())
    elif dq_2.qsize() > dq_1.qsize():
        dq_1.put(-dq_2.get())
        
for _ in range(int(input())):
    v, a = map(int, input().split())
    if a % 2 == 0:
        for i in range(2):
            add(v)
    elif a == 1:
        add(v)
    else:
        for i in range(3):
            add(v)
            
    if dq_1.qsize() > dq_2.qsize():
        print(-dq_1.queue[0])
    elif dq_2.qsize() > dq_1.qsize():
        print(dq_2.queue[0])
    else:
        print(min(dq_2.queue[0], -dq_1.queue[0]))
    