import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
dq.append([0, 0, 0])
while dq:
    x, y, cnt = dq.popleft()
    for x1, y1 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        xn, yn = x + x1, y + y1
        if xn < 0 or xn >= n or yn < 0 or yn >= m: continue
        if Map[xn][yn] == 1: continue
        Map[xn][yn] = 1
        if xn == n-1 and yn == m-1:
            print(cnt+1)
            sys.exit()
        dq.append([xn, yn, cnt + 1])
print(0)
